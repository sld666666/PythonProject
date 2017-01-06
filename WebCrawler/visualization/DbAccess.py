
from  database.MongodbDatabase import MongodbDatabase

KeyFinishedUrlsQuery = {"key":"finishedUrls"}
KeyTags = {"url" : "https://book.douban.com/tag/?view=type&icn=index-sorttags-all"}
class DbAccess:

    def __init__(self):
        self.db = MongodbDatabase()
        self.db.init('localhost', 27017, "book")

    def getUrlTree(self):
        rtn = self.db.get(KeyFinishedUrlsQuery)
        return rtn


    def getAllTags(self):
        rtn = self.db.get(KeyTags)
        return  rtn

