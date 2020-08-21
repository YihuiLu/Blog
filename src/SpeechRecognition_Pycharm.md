---
layout: post
title: MacOS 下 Pycharm运行SpeechRecognition无法录音
slug: SpeechRecognition
date: 2020-07-17 11:05
status: publish
author: 一灰
categories: 
  - SpeechRecognition
tags: 
  - 博客
  - SpeechRecognition
excerpt: 主要还是权限问题...
---

关联同样环境下的其他库和服务

比如：摄像头

因为涉及到调用硬件，MacOS会请求用户授权，由于2020.3以前的Pycharm并不兼容授权功能，导致代码运行不正常

解决方式：

建议直接在终端运行代码吧，

或者升级Pycharm到最新

也可以通过其他方法让Pycharm得到授权，但太麻烦了，得不偿失

