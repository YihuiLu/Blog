---
layout: post
title: 利用sqlacodegen自动生成ORM实体类
slug: mysql_group_by_1055
date: 2019-01-22 11:05
status: publish
author: 一灰
categories: 
  - Mysql
tags: 
  - 博客
  - Mysql
excerpt: 1055, "Expression #2 of SELECT list is not i...
---

今天在使用group_by时遇到错误，大概是以下样子：
```
(cymysql.err.InternalError) (1055, "Expression #2 of SELECT list is not in GROUP BY clause and contains nonaggregated column 
```
```
[SQL]CREATETABLE`m_part`(`f_id`INTNOTNULL,`f_name`VARCHAR(20)NULL,PRIMARYKEY(`f_id`))ENGINE=myisamDEFAULTCHARSET=utf8PARTITIONBYRANGE(f_id)(PARTITIONp0VALUESlessTHAN(10),PARTITIONp1VALUESlessTHAN(20))
```

原因：
mysql5.7.5版本开始，sql_mode使用的是默认值( 如上)，而之前使用的mysql配置文件中sql_mode=”“,由于这个特性使在使用group_by时出现报错

linux下解决方案：

修改**mysql.conf**

```
sudo vim /etc/mysql/mysql.conf.d/mysql.conf
```
然后将
```sql_mode=NO_ENGINE_SUBSTITUTION,STRICT_TRANS_TABLES ```
添加至文件末尾

重启服务：
```/etc/init.d/mysql restart```


问题解决