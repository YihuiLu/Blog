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
site_build_date = "2019-12-18T16:51+08:00"
author = "一灰"
email = "isRichard.Lu@gmail.com"
author_homepage = "https://github.com/YihuiLu"
description = "花径不曾缘客扫，蓬门今始为君开"
key_words = ['Maverick', '熊猫小A', 'Galileo', 'blog']
language = 'zh-CN'
external_links = [
    {
        "name": "吾爱破解",
        "url": "https://www.52pojie.cn/",
        "brief": "吾爱破解论坛致力于软件安全与病毒分析的前沿，丰富的技术版块交相辉映，由无数热衷于软件加密解密及反病毒爱好者共同维护."
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
    # {
    #     "name": "头痛记",
    #     "url": "${site_prefix}NoMigraine/",
    #     "target": "_self"
    # },
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
