---
layout: post
title: DBUtils 报错 codec can't encode characters in position
slug: redis
date: 2020-07-17 11:05
status: publish
author: 一灰
categories: 
  - DBUtils
tags: 
  - 博客
  - DBUtils
excerpt: 字符集问题...
---

今天使用DBUtils连接池遇到以下问题：
```
'latin-1' codec can't encode characters in position 74-75: ordinal not in range(256)
```
##解决方法：
>标准的连接方式相同，在初始化PooledDB时声明 charset=’utf8’

##代码如下：
```
pool = PooledDB(pymysql,

mincached=5,# 连接池里的最少连接数

                maxcached=30,#最大的空闲连接数，如果空闲连接数大于这个数，pool会关闭空闲连接

                maxshared=1000,#当连接数达到这个数，新请求的连接会分享已经分配出去的连接

                maxconnections=2000,#最大的连接数，

                blocking=True,#当连接数达到最大的连接数时，在请求连接的时候，如果这个值是True，请求连接的程序会一直等待，直到当前连接数小于最大连接数，如果这个值是False，会报错，

                host='rds93vu04hr3rn0o2d5io.mysql.rds.aliyuncs.com',

user='yd_loan_admin',

passwd='abcde123!@#',

db='yd_loan_sys',

port=3306,

charset='utf8')
```
##经过测试问题完美解决