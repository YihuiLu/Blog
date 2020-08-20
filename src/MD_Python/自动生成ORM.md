---
layout: post
title: 利用sqlacodegen自动生成ORM实体类
slug: sqlacodegen
date: 2018-8-12 15:05
status: publish
author: 一灰
categories: 
  - Python
tags: 
  - 博客
  - Python
excerpt: 某些特殊情况下我们需要反向生成ORM框架Model类...
---

**以下方法可以很方便的通过数据库表来生成ORM实体，节省某些特殊情况下攻城狮们的工作量**

命令：

```bash
sqlacodegen --noviews --noconstraints --noindexes --outfile d:\\models.py mysql://username:passwd@服务器地址:3306/dbname
```
| key  |  meaning   |
| :------------ | :------------ |
| noviews  |  不生成视图  |
| noconstraints  |  不生成外键关联  |
| noindexes  |  不生成索引  |
| outfile  |  文件输出路径  |

