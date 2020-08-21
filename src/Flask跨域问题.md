---
layout: post
title: Flask的跨域请求问题（CSRF）
slug: CSRF
date: 2019-07-27 1:05
status: publish
author: 一灰
categories: 
  - Python
tags: 
  - 博客
  - Python
excerpt: 跨域问题 “Cross-Origin Resource Sharing (CORS)” 的本质是 浏览器禁止从一个源加载的脚本与另一个源进行交互，即 —- 浏览器的同源策略
---

#前言：
   >**跨域问题**  *“Cross-Origin Resource Sharing (CORS)”* 的**本质**是 浏览器禁止从一个源加载的脚本与另一个源进行交互，即 --- ***浏览器的同源策略（Same-origin policy）***他的**定义**是：
>> The **same-origin policy** is a critical security mechanism that restricts how a document or script loaded from one [origin](https://developer.mozilla.org/en-US/docs/Glossary/origin "origin: Web content's origin is defined by the scheme (protocol), host (domain), and port of the URL used to access it. Two objects have the same origin only when the scheme, host, and port all match.") can interact with a resource from another origin. It helps to isolate potentially malicious documents, reducing possible attack vectors.
同源策略限制了从同一个源加载的文档或脚本如何与来自另一个源的资源进行交互。这是一个用于隔离潜在恶意文件的重要安全机制。

#经过：
   最近使用flask编写了一个前后端分离的web项目，前端对接时使用$.ajax，并且出现了如下问题：
![image.png](https://upload-images.jianshu.io/upload_images/9076474-05f27195b6a09b7a.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![image.png](https://upload-images.jianshu.io/upload_images/9076474-174e3c5b1e0dcdd2.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


#解决思路：
我们已经知道出现跨域问题的核心原因是浏览器的同源策略，所以解决问题的思路有两个：
* 从浏览器端解决
* 从服务器端解决

这次先谈如何从服务端解决，但是想要解决这个问题我们就需要搞明白到底什么是同源：

#####同源的定义：

如果两个页面的协议，端口（如果有指定）和域名都相同，则两个页面具有相同的**源**。

下表给出了相对`http://store.company.com/dir/page.html`同源检测的示例:

| URL | 结果 | 原因 |
| `http://store.company.com/dir2/other.html` | 成功 |  |
| `http://store.company.com/dir/inner/another.html` | 成功 |  |
| `https://store.company.com/secure.html` | 失败 | 不同协议 ( https和http ) |
| `http://store.company.com:81/dir/etc.html` | 失败 | 不同端口 ( 81和80) |
| `http://news.company.com/dir/other.html` | 失败 | 不同域名 ( news和store ) |

另请参见[文件的源定义: URLs](https://developer.mozilla.org/en-US/docs/Same-origin_policy_for_file:_URIs).

#解决方案

我们可以使用CORS的方式解决这个问题“Cross-Origin Resource Sharing (CORS)”

**什么是CORS？**

>Cross-Origin Resource Sharing ([CORS](https://developer.mozilla.org/en-US/docs/Glossary/CORS "CORS: CORS (Cross-Origin Resource Sharing) is a system, consisting of transmitting HTTP headers, that determines whether browsers block frontend JavaScript code from accessing responses for cross-origin requests.")) is a mechanism that uses additional [HTTP](https://developer.mozilla.org/en-US/docs/Glossary/HTTP "HTTP: The HyperText Transfer Protocol (HTTP) is the underlying network protocol that enables transfer of hypermedia documents on the Web, typically between a browser and a server so that humans can read them. The current version of the HTTP specification is called HTTP/2.") headers to tell a browser to let a web application running at one origin (domain) have permission to access selected resources from a server at a different origin. A web application makes a **cross-origin HTTP request** when it requests a resource that has a different origin (domain, protocol, and port) than its own origin.
跨源资源共享（[CORS](https://developer.mozilla.org/en-US/docs/Glossary/CORS "CORS：CORS（跨源资源共享）是一个系统，由传输HTTP标头组成，用于确定浏览器是否阻止前端JavaScript代码访问跨源请求的响应。")）是一种机制，它使用其他[HTTP](https://developer.mozilla.org/en-US/docs/Glossary/HTTP "HTTP：超文本传输​​协议（HTTP）是底层网络协议，它允许在Web上传输超媒体文档，通常在浏览器和服务器之间传输，以便人们可以读取它们。 HTTP规范的当前版本称为HTTP / 2。")标头告诉浏览器让在一个源（域）上运行的Web应用程序有权从不同来源的服务器访问所选资源。Web应用程序在请求具有与其自己的源不同的源（域，协议和端口）的资源时，会发出**跨源HTTP请求**。


一个跨域请求的例子：JavaScript的Web应用程序代码所服务的前端`http://domain-a.com`应用[`XMLHttpRequest`](https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest "使用XMLHttpRequest（XHR）对象与服务器进行交互。 您可以从URL检索数据，而无需进行整页刷新。 这使网页只更新页面的一部分，而不会中断用户正在做的事情。")做出了要求`http://api.domain-b.com/data.json`。

出于安全原因，浏览器会限制从脚本中发起的跨源HTTP请求。例如，`XMLHttpRequest`与[提取API](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API)遵循[同源策略](https://developer.mozilla.org/en-US/docs/Web/Security/Same-origin_policy)。这意味着使用这些API的Web应用程序只能从加载应用程序的同一源请求HTTP资源，除非来自其他来源的响应包含正确的CORS标头。

![image](http://upload-images.jianshu.io/upload_images/9076474-4b5467b967b622e0.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

CORS机制支持浏览器和Web服务器之间的安全跨源请求和数据传输。现代浏览器在API容器（如[Fetch](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API)`XMLHttpRequest`或[Fetch）中](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API)使用CORS 来帮助降低跨源HTTP请求的风险。

**如何在分flask中使用？**

代码示例：
```
from flask_cors import *

app = Flask(__name__)
CORS(app, supports_credentials=True)
```
亦或者你可以使用装饰器的方式为指定的视图函数进行配置
```
@app.route("/")
@cross_origin()
def helloWorld():
  return "Hello, cross-origin-world!"
```

flask中有随时可用的flask_cors 库，你可以直接调用他

以下是Flask-CORS 的官方文档链接

[http://flask-cors.readthedocs.io/en/latest/](http://flask-cors.readthedocs.io/en/latest/)

#原理？

>## Functional overview[Section](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS#Functional_overview)
>
>The Cross-Origin Resource Sharing standard works by adding new [HTTP headers](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers) that allow servers to describe the set of origins that are permitted to read that information using a web browser. Additionally, for HTTP request methods that can cause side-effects on server's data (in particular, for HTTP methods other than [`GET`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/GET "The HTTP GET method requests a representation of the specified resource. Requests using GET should only retrieve data."), or for [`POST`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/POST "The HTTP POST method sends data to the server. The type of the body of the request is indicated by the Content-Type header.") usage with certain [MIME types](https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types)), the specification mandates that browsers "preflight" the request, soliciting supported methods from the server with an HTTP [`OPTIONS`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/OPTIONS "The HTTP OPTIONS method is used to describe the communication options for the target resource. The client can specify a URL for the OPTIONS method, or an asterisk (*) to refer to the entire server.") request method, and then, upon "approval" from the server, sending the actual request with the actual HTTP request method. Servers can also notify clients whether "credentials" (including [Cookies](https://developer.mozilla.org/en-US/docs/Web/HTTP/Cookies) and HTTP Authentication data) should be sent with requests.
CORS failures result in errors, but for security reasons, specifics about what went wrong *are not available to JavaScript code*. All the code knows is that an error occurred. The only way to determine what specifically went wrong is to look at the browser's console for details.
Subsequent sections discuss scenarios, as well as provide a breakdown of the HTTP headers used.
跨源资源共享标准的工作原理是添加新的[HTTP标头](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers)，允许服务器描述允许使用Web浏览器读取该信息的起源集。此外，对于可能对服务器数据产生副作用的HTTP请求方法（特别是对于除某些[MIME类型](https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types)以外的HTTP方法[`GET`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/GET "HTTP GET方法请求指定资源的表示。 使用GET的请求应该只检索数据。")或用于[`POST`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/POST "HTTP POST方法将数据发送到服务器。 请求正文的类型由Content-Type标头指示。")某些[MIME类型](https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types)），规范要求浏览器“预检”请求，从而请求支持的方法。服务器使用HTTP [`OPTIONS`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/OPTIONS "HTTP OPTIONS方法用于描述目标资源的通信选项。 客户端可以指定OPTIONS方法的URL，也可以指定星号（*）来引用整个服务器。")请求方法，然后，在服务器“批准”后，使用实际的HTTP请求方法发送实际请求。服务器还可以通知客户端是否“凭据”（包括[Cookie）](https://developer.mozilla.org/en-US/docs/Web/HTTP/Cookies) 和HTTP认证数据）应该与请求一起发送。
>
>CORS失败会导致错误，但出于安全原因，*JavaScript代码无法使用*有关错误*的详细信息*。所有代码都知道发生了错误。确定具体问题的唯一方法是查看浏览器的控制台以获取详细信息。


仓促整理，不喜勿喷

