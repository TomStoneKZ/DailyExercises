#-*- coding: utf-8 -*-

import urllib2
import urllib
import re

#百度贴吧爬虫类
class BDTB:

    #初始化，传入基地址，是否只看楼主的参数
    def __init__(self, baseurl,see_lz):
        self.baseurl = baseurl
        self.see_lz = 'see_lz=' + str(see_lz)

    #传入页码，获取该页帖子的代码
    def getPage(self, pageNum):
        try:
            url = self.baseurl + self.see_lz + '&pn=' + str(pageNum)
            user_agent = "Mozilla/5.0 (Windows NT 6.3; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0"
            headers = {'User-Agent': user_agent}
            request = urllib2.Request(url, headers=headers)
            response = urllib2.urlopen(request)
            return response.read().decode('utf-8')
        except urllib2.URLError, e:
            if hasattr(e, "reason"):
                print u"连接百度贴吧失败，错误原因", e.reason
                return None

    def getTitle(self):
        page = self.getPage(1)
        pattern = re.compile('<h3 class="core_title_txt.*?>(.*?)</h3>', re.S)
        result = re.search(pattern, page)
        return result.group(1).strip()


baseurl = 'http://tieba.baidu.com/p/3138733512?'
bdtb = BDTB(baseurl, 1)
print bdtb.getTitle()


