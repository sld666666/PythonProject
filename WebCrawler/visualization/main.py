import sys
import os
parent = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
sys.path.append(parent)
print(sys.path)

from  database.MongodbDatabase import MongodbDatabase
from visualization.CsvParser import CsvWriter
from visualization.DbAccess import  DbAccess

if "__main__" == __name__:
    dbAccess = DbAccess()
    urlTree = dbAccess.getUrlTree()



def test1():
    db = MongodbDatabase()
    print("begin")
    db.init('115.28.83.94', 27017, "book")
    rtns =db.get({})

    books = []
    for rtn in  rtns:
        if 'content' not in rtn:
            continue

        onebooks = rtn['content']
        books.append(onebooks)

    #sorted(books, key=lambda book:book['score'])
    print('get books')
    csvWriter = CsvWriter()
    csvWriter.write('result.csv', books)
    print('finished')

