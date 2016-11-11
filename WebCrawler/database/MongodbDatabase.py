from WebCrawler.database.IDatabase import IDatabase
import pymongo

class MongodbDatabase(IDatabase):

    def init(self, ip, host, dbname):
        client =  pymongo.MongoClient(ip,host)
        self.connection = client[dbname][dbname]

    def get(self, key):
        return self.connection.find(key)

    def add(self, value):
        self.connection.insert(value)

    def update(self, key, value):
        self.connection.update(key, value)


    def delete(self, key):
        return self.connection.remove(key)