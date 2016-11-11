
import WebCrawler.biz.doubanbooks.BooksPage as BP
import WebCrawler.biz.doubanbooks.TagsPage as TP
import WebCrawler.biz.doubanbooks.SubjectPage as SP
from  WebCrawler.network.CrawlerManager import CrawlerMannager
import logging
import sys

def initLog():
     logging.basicConfig(
        filename='webcrawler.log',
        level=logging.DEBUG
    )

def initSys():
    pass

def begin():
    dbConfig = {'ip':'localhost', 'port':27017,'dbName':'book'}
    manager = CrawlerMannager(dbConfig)
    manager.register(BP.BooksPage())
    manager.register(TP.TagsPage())
    manager.register(SP.SubjectPage())

    manager.setBaseUrl("https://book.douban.com")

    logging.debug("begin")
    rtn = manager.excute('https://book.douban.com/tag/?view=type&icn=index-sorttags-all', None)
    logging.debug(rtn)
    print("finished")


if __name__=='__main__':
    initSys()
    initLog()
    begin()

