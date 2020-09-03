---
layout: post
title: Linux 下安装Java 14（适用大多数Linux发行版）
slug: java
date: 2020-9-3 13:34
status: publish
author: 一灰
categories: 
  - Java
tags: 
  - 博客
  - Celery Flask
excerpt: 
---

###1. 在/usr/下创建java目录

```
root@9314e39c1d8c: mkdir/usr/java
root@9314e39c1d8c: cd /usr/java
```

###2. 下载Java压缩文件并解压

```
root@9314e39c1d8c: curl -O curl -O https://download.oracle.com/otn-pub/java/jdk/14.0.2+12/205943a0976c4ed48cb16f1043c5c647/jdk-14.0.2_linux-x64_bin.tar.gz?AuthParam=1599111678_3050bd9ff5d540cc544a0567b2d3e31f
root@9314e39c1d8c: tar -zxvf jdk-14.0.2_linux-x64_bin.tar.gz\?AuthParam\=1599111678_3050bd9ff5d540cc544a0567b2d3e31f
```
也可以来这里下载自己需要的版本：
[https://www.oracle.com/cn/java/technologies/javase-downloads.html](https://www.oracle.com/cn/java/technologies/javase-downloads.html)
下载完以后自行调整安装指令


###3. 设置环境变量

```
root@9314e39c1d8c: vi /etc/profile
```
在文件最后添加如下内容
```
JAVA_HOME=/usr/java/jdk-14.0.2
JRE_HOME=/usr/java/jdk-14.0.2/jre
CLASS_PATH=.:$JAVA_HOME/lib/dt.jar:$JAVA_HOME/lib/tools.jar:$JRE_HOME/lib
PATH=$PATH:$JAVA_HOME/bin:$JRE_HOME/bin
export JAVA_HOME JRE_HOME CLASS_PATH PATH
```

###4. 更新配置

```root@9314e39c1d8c: source /etc/profile```

###5. 验证

```
root@9314e39c1d8c:/usr/java# java --version
java 14.0.2 2020-07-14
Java(TM) SE Runtime Environment (build 14.0.2+12-46)
Java HotSpot(TM) 64-Bit Server VM (build 14.0.2+12-46, mixed mode, sharing)
```


# 大功告成