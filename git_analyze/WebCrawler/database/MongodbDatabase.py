from database.IDatabase import IDatabase
import pymongo

USENAME = 'sld'
PASSWORLD = 'sld123'
class MongodbDatabase(IDatabase):

    def init(self, ip, host, dbname):
        url = 'mongodb://{}:{}@{}:{}'.format(USENAME, PASSWORLD,ip,host)
        client =  pymongo.MongoClient(url)
        self.connection = client[dbname][dbname]

    def get(self, key):
        return self.connection.find(key)

    def add(self, value):
        self.connection.insert(value)

    def update(self, key, value):
        self.connection.update(key, value)


    def delete(self, key):
        return self.connection.remove(key)