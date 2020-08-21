---
layout: post
title: Python时间处理小结
slug: datetime
date: 2017-07-17 11:05
status: publish
author: 一灰
categories: 
  - Python
tags: 
  - 博客
  - Python
excerpt: 
---


```import datetime

nowTime=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')#现在

pastTime = (datetime.datetime.now()-datetime.timedelta(hours=1)).strftime('%Y-%m-%d %H:%M:%S')#过去一小时时间

afterTomorrowTime = (datetime.datetime.now()+datetime.timedelta(days=2)).strftime('%Y-%m-%d %H:%M:%S')#后天

tomorrowTime = (datetime.datetime.now()+datetime.timedelta(days=1)).strftime('%Y-%m-%d %H:%M:%S')#明天

print('\n',nowTime,'\n',pastTime,'\n',afterTomorrowTime,'\n',tomorrowTime)
```


python简单获取两个日期之间的年度、月度、天数差的方法


```
import datetime

def days(str1,str2):

date1=datetime.datetime.strptime(str1[0:10],"%Y-%m-%d")

date2=datetime.datetime.strptime(str2[0:10],"%Y-%m-%d")

num=(date1-date2).days

return num

def months(str1,str2):

year1=datetime.datetime.strptime(str1[0:10],"%Y-%m-%d").year

year2=datetime.datetime.strptime(str2[0:10],"%Y-%m-%d").year

month1=datetime.datetime.strptime(str1[0:10],"%Y-%m-%d").month

month2=datetime.datetime.strptime(str2[0:10],"%Y-%m-%d").month

num=(year1-year2)*12+(month1-month2)

return num

输入days('2018-04-23 08:18:09','2017-03-21 10:19:33') ，返回398

输入months('2018-01-23 08:18:09','2017-03-21 10:19:33')，返回10
import datetime

nowTime=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')#现在

pastTime = (datetime.datetime.now()-datetime.timedelta(hours=1)).strftime('%Y-%m-%d %H:%M:%S')#过去一小时时间

afterTomorrowTime = (datetime.datetime.now()+datetime.timedelta(days=2)).strftime('%Y-%m-%d %H:%M:%S')#后天

tomorrowTime = (datetime.datetime.now()+datetime.timedelta(days=1)).strftime('%Y-%m-%d %H:%M:%S')#明天

print('\n',nowTime,'\n',pastTime,'\n',afterTomorrowTime,'\n',tomorrowTime)
```~~~~