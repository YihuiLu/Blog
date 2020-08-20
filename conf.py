# -*- coding: utf-8 -*-
"""博客构建配置文件 
"""

# For Maverick
site_prefix = "/Blog/"
source_dir = "../src/"
build_dir = "../dist/"
index_page_size = 10
archives_page_size = 20
template = {
    "name": "Galileo",
    "type": "local",
    "path": "../Galileo"
}
enable_jsdelivr = {
    "enabled": True,
    "repo": "YihuiLu/Blog@gh-pages"
}

# 站点设置
site_name = "一灰的技术博客"
site_logo = "${static_prefix}logo.png"
site_build_date = "2019-2-18T16:51+08:00"
author = "一灰"
email = "isRichard.Lu@gmail.com"
author_homepage = "https://github.com/YihuiLu"
description = "花径不曾缘客扫，蓬门今始为君开"
key_words = ['Maverick', '一灰', '头痛记', 'blog']
language = 'zh-CN'
external_links = [
    {
        "name": "吾爱破解",
        "url": "https://www.52pojie.cn/",
        "brief": "一个一灰常逛的论坛~"
    },
    {
        "name": "一灰小站",
        "url": "https://www.yifeilu.cn",
        "brief": "一灰的旧主页。"
    }
]
nav = [
    {
        "name": "首页",
        "url": "${site_prefix}",
        "target": "_self"
    },
    {
        "name": "归档",
        "url": "${site_prefix}archives/",
        "target": "_self"
    },
    {
        "name": "头痛记",
        "url": "${site_prefix}Migraine/",
        "target": "_self"
    },
    {
        "name": "关于",
        "url": "${site_prefix}about/",
        "target": "_self"
    }
]

social_links = [
    # {
    #     "name": "Twitter",
    #     "url": "https://twitter.com/AlanDecode",
    #     "icon": "gi gi-twitter"
    # },
    {
        "name": "GitHub",
        "url": "https://github.com/YihuiLu",
        "icon": "gi gi-github"
    },
    # {
    #     "name": "Weibo",
    #     "url": "https://weibo.com/5245109677/",
    #     "icon": "gi gi-weibo"
    # }
]

head_addon = r'''
<meta http-equiv="x-dns-prefetch-control" content="on">
<link rel="dns-prefetch" href="//cdn.jsdelivr.net" />
'''

footer_addon = ''

body_addon = ''

valine = {
    "enable": True,
    "el": '#vcomments',
    "appId": "FHu0SCPDeyBjMY4s0ECouzDf-gzGzoHsz",
    "appKey": "UecRNirhvv66x0fxlpKjmFSk",
}
