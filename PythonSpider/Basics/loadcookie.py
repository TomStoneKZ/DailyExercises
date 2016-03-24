#coding=utf-8

import urllib2
import cookielib

#创建MozillaCookieJar实例对象
cookie = cookielib.MozillaCookieJar()
#从文件中读取cookie内容到变量
cookie.load('cookie.txt', ignore_discard=True, ignore_expires=True)
#创建请求的request
request = urllib2.Request('http://baidu.com')
#利用urllib2的build_opener方法创建一个opener
handler = urllib2.HTTPCookieProcessor(cookie)
opener = urllib2.build_opener(handler)
response = opener.open(request)
print(response.read())
