import copy
import logging
import time

from database.MongodbDatabase import MongodbDatabase
from network.HttpUrlContentFetcher import HttpUrlContentFetcher
from parserer.Parser import Parser

FinishedUrlsQuery = {"key":"finishedUrls"}
ChildrenKey = "children"

class CrawlerMannager:

    def __init__(self, dbConfig):
        self.contentFetcher = HttpUrlContentFetcher()
        self.parser = Parser()
        self.pages = []
        self.finishedUrls = FinishedUrls()

        self.database = MongodbDatabase()
        self.database.init(dbConfig['ip'], dbConfig['port'], dbConfig['dbName'])
        if  self.database.get(FinishedUrlsQuery).count() <= 0:
            tmp = copy.deepcopy(FinishedUrlsQuery)
            tmp.update({'value':{}})
            self.database.add(tmp)
        else:
            finishedUrlDict = self.database.get(FinishedUrlsQuery)[0]['value']
            if len(finishedUrlDict) > 0:
                self.finishedUrls = FinishedUrls.fromDict(finishedUrlDict)

    def init(self, indexUrl, tag):
        content = self.contentFetcher.getContentInBytes(indexUrl)
        self.contentFetcher.setCodec(self.contentFetcher.getcodec(content)['encoding'])
        self.tag = tag

    def setBaseUrl(self, url):
        self.baseUrl = url


    def register(self, page):
        self.pages.append(page)

    def excute(self, url, parentUrl):
        if self.finishedUrls.isFinished(url):
            return

        self.saveUrl(url, parentUrl)
        print(url)
        time.sleep(1)

        curPage = self.getPage(url)
        if None == curPage:
            logging.debug("#not find page %s", url)
            return

        rtn = self.contentFetcher.fetcher(url)
        if None == rtn:
            return

        soup = self.parser.parser(str(rtn))

        nextUrls = []
        pageContent = curPage.analysis(soup, nextUrls)
        self.save(url, pageContent)

        for nextUrl in nextUrls:
            if None == nextUrl: continue

            self.excute(self.getNexPageUrl(nextUrl), url)

    def saveUrl(self, url, parentUrl):
        FinishedUrls.add(self.finishedUrls, url, parentUrl)
        tmp = {'value':FinishedUrls.toDict(self.finishedUrls)}
        tmp.update(FinishedUrlsQuery)
        self.database.update(FinishedUrlsQuery, tmp)

    def getPage(self, url):
        for page in self.pages:
            keyword = page.getKeyword()
            if type(keyword) is list:
                for one in keyword:
                    if url.find(one) > 0 :
                        return  page
            else:
                if url.find(page.getKeyword()) > 0 :
                    return page

        return None

    def getNexPageUrl(self, url):
        if  url.find('http://') < 0 and  url.find('https://') < 0:
            url  = self.baseUrl + url

        return url

    def save(self, url, content):
        tmp = {}
        tmp['url'] = url
        tmp['content'] = content
        tmp['tag']= self.tag
        self.database.add(tmp)
        pass


class FinishedUrls:

    def __init__(self):
        self.current = ""
        self.children = []

    def getCurrent(self):
        return  self.current

    def setCurrent(self, url):
        self.current = url

    def getChildren(self):
        return  self.children

    def addChild(self, url):
        finishedUrl = FinishedUrls()
        finishedUrl.setCurrent(url)
        self.children.append(finishedUrl)

    def isFinished(self, url):
        rtn = False

        if self.current == url and len(self.children) <= 0:
            rtn = True
        else:
            for child in self.children:
                rtn = child.isFinished(url)
                if  rtn:
                    break

        return  rtn
    @staticmethod
    def add(finishedUrls, url, parentUrl):
        if None == parentUrl:
            finishedUrls.setCurrent(url)
        elif len(finishedUrls.getCurrent())==0:
            finishedUrls.setCurrent(url)
        elif finishedUrls.getCurrent() == parentUrl:
            finishedUrls.addChild(url)
        else:
            for child in finishedUrls.getChildren():
                FinishedUrls.add(child, url, parentUrl)

    @staticmethod
    def toDict(finishedUrls):
        rtn = {'current':finishedUrls.getCurrent()}

        chilrenDict = []
        for child in finishedUrls.getChildren():
            tmp = FinishedUrls.toDict(child)
            chilrenDict.append(tmp)

        rtn[ChildrenKey] = chilrenDict
        return rtn

    @staticmethod
    def fromDict(finishedUrlDict):
        rtn =  FinishedUrls()
        rtn.setCurrent(finishedUrlDict['current'])
        if ChildrenKey in finishedUrlDict:
            children = finishedUrlDict[ChildrenKey]

            for child in children:
                oneFinshed = FinishedUrls.fromDict(child)
                rtn.children.append(oneFinshed)

        return  rtn

            