---
layout: post
title: MySQL & SQLit忽略外键约束删除数据
slug: FOREIGN_KEY_CHECKS
date: 2019-02-22 9:05
status: publish
author: 一灰
categories: 
  - Mysql
tags: 
  - 博客
  - Mysql
excerpt: 关闭外键校验
---

今天在删除表数据时遇到一个问题：

```
ERROR 1701 (42000): Cannot truncate a table referenced
in a foreign key constraint
(`diandian_loan`.`auth_group_permissions`, CONSTRAINT 
`auth_group_permissi_permission_id_84c5c92e_fk_auth_p
ermission_id` FOREIGN KEY (`permission_id`) REFERENCES 
`diandian_loan`.`auth_permissio)
```

意思是由于有**主外键约束**，所以不能删除表数据。

即使当时已经将父表数据清空还是不行。



### 解决办法：

先取消主外键关系验证：
```sql
SET FOREIGN_KEY_CHECKS = 0;
```

然后删除需要删除的数据

最后恢复：
```sql
SET FOREIGN_KEY_CHECKS = 1;
```


SQLit略有不同

```sql
PRAGMA foreign_keys = 0;
```

```sql
PRAGMA foreign_keys = 1;
```

*完美解决*
