---
layout: post
title: 小记一次FastAPI使用连接池调用Redis时，切换数据库的问题
slug: FastAPI Redis aioredis
date: 2021-03-11 17:38
status: publish
author: 一灰
categories: 
  - FastAPI
tags: 
  - 博客
  - FastAPI
  - Redis
excerpt: 实现自动切换连接池 
---


之前因为项目需要，尝试了新兴框架 FastAPI，他的很多特性十分值得称赞，比如自动文档、类型校验、速度、异步等等

但是在使用过程中遇到了切换Redis db的需求，比如验证码、用户登录信息等等的缓存需要通过db隔离，因为FastApi的异步特性，当时选用了aioredis
作为驱动，但是翻了翻文档并没有找到在创建连接池后切换数据库的方法，于是参考了Django框架的实现原理：给每一个db单独创建连接池，在使用时根据需求调用即可

于是编写代码如下：

```python
class RedisPool:
    redis_pool_dict = {}

    def __await__(self):
        self._create_pool()
        return self._create_pool().__await__()

    async def _create_pool(self):
        for i in settings.REDIS_DB_LIST:
            redis = await aioredis.create_redis_pool(
                settings.REDIS_URL + "{db}?encoding=utf-8".format(db=i)
            )
            self.redis_pool_dict.update({i: redis})
        return self

    def select_db(self, db=52):
        c = self.redis_pool_dict[db]
        if not c:
            raise ValueError('调用的Redis数据库未创建连接池')
        return c

    def close_pool(self):
        for i in self.redis_pool_dict.values():
            i.close()

```

结合框架如下：

```python
def register_redis(app: FastAPI) -> None:
    @app.on_event("startup")
    async def create_redis():
        app.state.redis = await RedisPool()

    @app.on_event("shutdown")
    async def close_redis():
        app.state.redis.close_pool()
```

调用方法如下：

```python
redis_client = request.app.state.redis.select_db(db=53)
rs = await redis_client.set(
        key="test_key-",
        value="12",
        expire=60 * 60 * 4  # token过期时间为4小时
    )
```

大概逻辑如下：
1. 迭代配置文件声明的，需要使用的db列表
2. 创建每个db的pool
3. 使用时找到需要的拿去用即可

其他：
1. 在框架启动时利用FastAPI的@app.on_event("startup")初始化连接池
2. 在框架关闭时close_pool()


上面值得注意的是，因为aioredis是异步的，所以一处异步处处异步
异步类不常写，所以记录一下
