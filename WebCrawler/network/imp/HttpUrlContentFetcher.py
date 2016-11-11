
import urllib
import urllib.request
from urllib import parse
import logging
import http.cookiejar
import gzip
import io

Headers = {'Connection':'keep-alive',
            'Cache-Control': 'max-age=0',
           'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
           'Upgrade-Insecure-Requests': '1',
            'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2467.2 Safari/537.36',
           'Accept-Charset':'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
           'Accept-Encoding':'gzip, deflate, sdch',
           'Accept-Language':'zh-CN,zh;q=0.8,en;q=0.6'
           #'Referer':'book.douban.com'
}

CookieFilename = 'cookie.txt'
class HttpUrlContentFetcher :
    def __init__(self):
        self.cookie = None

    def fetcher(self, url):
        parserResult = parse.urlparse(url)
        parserResult = parserResult._replace(path= urllib.parse.quote(parserResult.path))
        url = parse.urlunparse(parserResult)
        try:
            if None == self.cookie:
                self.cookie = self.getCookie(url)

            handler = urllib.request.HTTPCookieProcessor(self.cookie)
            opener = urllib.request.build_opener(handler)
            req = urllib.request.Request(url, headers=Headers)
            response = opener.open(req)
            gzip_f = gzip.GzipFile(fileobj=io.BytesIO(response.read()))
            content = gzip_f.read()
            html = content.decode('UTF-8')
        except Exception as e:
            logging.error('#fetchr url:%s', url + ":" + str(e))
            html=None

        return html

    def getCookie(self, url):
        try:
            cookie = http.cookiejar.MozillaCookieJar(CookieFilename)
            cookie.load(CookieFilename, ignore_discard=True, ignore_expires=True)
            return  cookie
        except Exception as e:
            return  self.saveCookie(url)

    def saveCookie(self, url):
        try:
            cookie = http.cookiejar.MozillaCookieJar(CookieFilename)
            handler = urllib.request.HTTPCookieProcessor(cookie)
            opener = urllib.request.build_opener(handler)
            req = urllib.request.Request(url, headers=Headers)
            response = opener.open(req)
            cookie.save(ignore_discard=True, ignore_expires=True)
            return  cookie
        except Exception as e:
            return  None
