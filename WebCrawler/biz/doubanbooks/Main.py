
import sys
import os
parent = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
parent = os.path.abspath(os.path.join(parent, os.pardir))
sys.path.append(parent)
print(sys.path)

import biz.doubanbooks.BooksPage as BP
import biz.doubanbooks.TagsPage as TP
import biz.doubanbooks.SubjectPage as SP
from  network.CrawlerManager import CrawlerMannager
import logging

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

