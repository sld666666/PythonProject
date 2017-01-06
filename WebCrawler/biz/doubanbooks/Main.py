
import sys
import os
parent = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
parent = os.path.abspath(os.path.join(parent, os.pardir))
sys.path.append(parent)
print(sys.path)

import biz.doubanbooks.BooksPage as BP
import biz.doubanbooks.TagsPage as TP
import biz.doubanbooks.SubjectPage as SP
import biz.cnblogs.IndexPage as IP
import biz.cnblogs.OnePagePage as OPP
from  network.CrawlerManager import CrawlerMannager
import logging

DoubanIndexUrl = 'https://book.douban.com/tag/?view=type&icn=index-sorttags-all'
CnBlogIndexUrl = 'http://www.cnblogs.com/sld666666/default.html'
DoubanBaseUrl = 'https://book.douban.com'
def initLog():
     logging.basicConfig(
        filename='webcrawler.log',
        level=logging.DEBUG
    )

def initSys():
    pass

def begin(indexUrl, dbNamme, baseUrl):
    dbConfig = {'ip':'localhost', 'port':27017,'dbName':dbNamme}
    manager = CrawlerMannager(dbConfig)
    manager.register(BP.BooksPage())
    manager.register(TP.TagsPage())
    manager.register(SP.SubjectPage())
    manager.register(IP.IndexPage())
    manager.register(OPP.OnePagePage())

    manager.setBaseUrl(baseUrl)

    logging.debug("begin")
    rtn = manager.excute(indexUrl, None)
    logging.debug(rtn)
    print("finished")


if __name__=='__main__':
    initSys()
    initLog()
    begin(CnBlogIndexUrl, 'sld_blog', CnBlogIndexUrl)

