---
layout: post 
title: 解决 M1 Mac 'has no attribute 'enable_load_extension'
slug: M1 Mac 'has no attribute 'enable_load_extension' 
date: 2021-08-09 19:46 
status: publish 
author: 一灰 
categories:
  - Sqlite 
tags:
  - 博客
  - Sqlite
  - Python
  - M1 
excerpt: 通过重新编译Python解决
---


最近由于项目需要，使用```spatialite```插件，但是实际使用时遇到以下错误

```shell

AttributeError: 'sqlite3.Connection' object has no attribute 'enable_load_extension'
```

废了点心思，最终在Python3.9文档中找到如下描述：

> sqlite3 模块的构建默认没有附带可加载扩展支持，因为某些平台（特别是 Mac OS X）上的 SQLite 库在编译时未使用此特性。 要获得可加载扩展支持，你必须传入 --enable-loadable-sqlite-extensions 来进行配置。

描述比较清晰，主要是因为系统环境，导致编译时未打开```enable-loadable-sqlite-extensions```

于是尝试了几个版本的python以后，最终成功编译 [python3.8.10](https://www.python.org/ftp/python/3.8.10/Python-3.8.10.tgz)

编译流程：

1. 下载 [python3.8.10](https://www.python.org/ftp/python/3.8.10/Python-3.8.10.tgz) 到本地
2. 解压到任意目录
3. ```shell 
   cd /解压目录
   
   ./configure --enable-loadable-sqlite-extensions  
   # --enable-loadable-sqlite-extensions是关键

   make

   make install 
   
   # 可能会出现缺少依赖无法编译的问题，可以根据实际报错处理
   ```


最后经过测试可以完美调用 ```enable_load_extension``` 函数
