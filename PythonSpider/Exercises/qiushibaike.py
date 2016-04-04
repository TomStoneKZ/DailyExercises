# -*- coding: utf-8 -*-

import urllib2
import urllib
import re

page = 1
url = 'http://qiushibaike.com/hot/page' + str(page)
#user_agent = 'Mozilla/4.0(compatible; MSIE 5.5; Windows NT)'
user_agent = "Mozilla/5.0 (Windows NT 6.3; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0"
headers = {'User-Agent' : user_agent}
try:
    request = urllib2.Request(url, headers=headers)
    response = urllib2.urlopen(request)
    content = response.read().decode('utf-8')
    pattern = re.compile('<div.*?author clearfix">.*?<a.*?<img.*?>(.*?)</a>.*?<div.*?' +
                         'content">(.*?)<!--(.*?)-->.*?</div>(.*?)<div class="stats.*?class="number">(.*?)</i>', re.S)
    items = re.findall(pattern, content)
    for item in items:
        haveImg = re.search("img", item[3])
        if not haveImg:
            print item[1]
except urllib2.URLError, e:
    if hasattr(e, "code"):
        print e.code
    if hasattr(e, "reason"):
        print e.reason
