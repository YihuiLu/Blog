---
layout: post
title: Celery+jpype 卡死，Celery+Java 卡死，Celery Task 卡死
slug: Celery
date: 2020-9-8 16:58
status: publish
author: 一灰
categories: 
  - Python
tags: 
  - 博客
  - Flask
  - Celery
  - jpype
excerpt: 
---

最近在写一个项目的时候同时使用到了```Celery```和```jpype```

但是在实际使用过程中出现了Celery Task进程卡死的情况

解决思路如下：

首先是观察到涉及到使用```jpype```的代码在本地运行没有问题，代码片段如下：

```python
from jpype import *

...

def load_trie(src):
    maps = JClass('java.util.TreeMap')()  # 创建 TreeMap 空间

    for word in src:
        word = word.strip()
        maps[word] = word
    rs = JClass('com.hankcs.hanlp.collection.trie.DoubleArrayTrie')(maps)
    return rs

...

```

经过排错后发现代码停止在以下位置：

```python
rs = JClass('com.hankcs.hanlp.collection.trie.DoubleArrayTrie')(maps)
```

这段代码调用了Java相关的包，于是Google到了以下内容
[https://github.com/jpype-project/jpype/issues/358](https://github.com/jpype-project/jpype/issues/358)

在这个issues中提到了：
>Wow that is failing in a very strange spot. When you said failed in a thread I figured it would be in the proxy code, but this is a fail on getting environment variables on startup. Are you sure that you don't have more than one JVM started? Your module doesn't do a check for isJVMStarted, but I thought that we have explicit checks to prevent a fail there so that seems unlikely. The trace also does not show a second call.
>My next best guess is this is a security violation. I don't know much about celery, but it may be possible that it is trying to start the JVM from within some type of sand box. My approach would be to instrument the call to JPEnv::CreateJavaVM to record all the inputs that are being passed to JVM and see if I was sure that nothing bad got sent to the JVM call. As you can see in the trace, we haven't even made contact with the JVM, so assuming we are providing it with valid inputs the bug is likely in the JVM and not within JPype.
>The last option here though it seems unlikely is the shared memory loader for the jvm has somehow failed. The only thing that we do with the JVM before this point is loading the shared library into memory. On architectures with mixed executable files (32/64) this can often go wrong leading to a bad entry point. But as you ran to the Parse locale it seems unlikely.

>```
>C  [libjava.dylib+0xd2a7]  getMacOSXLocale+0x123
>C  [libjava.dylib+0xd353]  setupMacOSXLocale+0x12
>C  [libjava.dylib+0xd765]  ParseLocale+0x2e
>C  [libjava.dylib+0xd4ef]  GetJavaProperties+0x183
>C  [libjava.dylib+0x5cbb]  Java_java_lang_System_initProperties+0x30
>j  java.lang.System.initProperties(Ljava/util/Properties;)Ljava/util/Properties;+0
>j  java.lang.System.initializeSystemClass()V+13
>v  ~StubRoutines::call_stub
>V  [libjvm.dylib+0x2f0b3a]
>V  [libjvm.dylib+0x2f0d35]
>V  [libjvm.dylib+0x2f0ead]
>V  [libjvm.dylib+0x57313b]
>V  [libjvm.dylib+0x3271b2]
>C  [_jpype.cpython-36m-darwin.so+0x242cb]  _ZN5JPEnv12CreateJavaVMEPv+0x3b
>The specific failure point is
>
>  // Get the entry points in the shared library
>  loadEntryPoints(vmPath);  <== Could load invalid pointers
>
>  JavaVMInitArgs jniArgs;
>  jniArgs.options = NULL;
>
>  // prepare this ...
>  jniArgs.version = USE_JNI_VERSION;
>  jniArgs.ignoreUnrecognized = ignoreUnrecognized;
>
>  jniArgs.nOptions = (jint)args.size();
>  jniArgs.options = (JavaVMOption*)malloc(sizeof(JavaVMOption)*jniArgs.nOptions);
>  memset(jniArgs.options, 0, sizeof(JavaVMOption)*jniArgs.nOptions);
>  for (int i = 0; i < jniArgs.nOptions; i++)
>  {
>    jniArgs.options[i].optionString = (char*)args[i].c_str();  <== All options should be valid
>  }
>  JPEnv::CreateJavaVM((void*)&jniArgs);  <== Everything in the structure should be valid at this point
>  free(jniArgs.options);
>The only trace I could find that was similar is
>
>https://bugs.openjdk.java.net/secure/attachment/72587/hs_err_pid55488.log
>```

再加上这个issues中的其他信息，猜测是在```celery```的```worker```中因为某种环境的影响导致```Java```无法正常运行，并与```JVM```有关

并且最后他们提到
> Starting after the fork is by far the safest approach.

然后这个问题还关闭了，这就郁闷了，但请教同事建议我看了这个：
[https://stackoverflow.com/questions/12003221/celery-task-schedule-ensuring-a-task-is-only-executed-one-at-a-time](https://stackoverflow.com/questions/12003221/celery-task-schedule-ensuring-a-task-is-only-executed-one-at-a-time)

最后找到了：[https://docs.celeryproject.org/en/stable/reference/celery.bin.worker.html#cmdoption-celery-worker-p](https://docs.celeryproject.org/en/stable/reference/celery.bin.worker.html#cmdoption-celery-worker-p)

猜测跟worker运行时的线程约束有关，于是乎测试：

```
-P, --pool
Pool implementation:

prefork (default), eventlet, gevent, threads or solo.
```


##然后就顺利的成功了

最后的worker启动命令如下：

```
celery -A celery_app.worker:celery worker -c 4 -l info -P solo
```

重点在于
```
-P solo
```
这个命令指定了每个worker只能用单线程模式执行，这样就不会导致JVM出现不可预知的问题

经过测试在指定 ```-P solo``` 的同时可以指定 ```-c  ```


仓促记录，日后修改