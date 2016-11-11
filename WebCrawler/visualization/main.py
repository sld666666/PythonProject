

from  WebCrawler.database.MongodbDatabase import MongodbDatabase
from WebCrawler.visualization.CsvParser import CsvWriter

if "__main__" == __name__:
    db = MongodbDatabase()
    print("begin")
    db.init('localhost', 27017, "book")
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
    i = 0