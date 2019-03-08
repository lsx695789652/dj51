# coding:utf-8
import urllib.request


class reqdata(object):
    def requrl(self, url):
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req) as response:
            data = response.read()
            htmlstr = data.decode()
            return htmlstr
        return None
