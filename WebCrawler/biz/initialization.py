import logging
from  network.CrawlerManager import CrawlerMannager

def initSys():
    pass

def getDbmanager(dbNamme):
    dbConfig = {'ip':'115.28.83.94', 'port':27017,'dbName':dbNamme}
    manager = CrawlerMannager(dbConfig)
    return manager

def initLog():
     logging.basicConfig(
        filename='webcrawler.log',
        level=logging.DEBUG
    )
