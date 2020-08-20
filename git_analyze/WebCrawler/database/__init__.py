
from database.IDatabase import IDatabase
from  database.MongodbDatabase import MongodbDatabase

if __name__ == '__main__':
    database = MongodbDatabase()
    database.init("localhost", 27017, "book")
    n1 = {"title":"java", "name":"Bush"}
    n2 = {"title":"fortran", "name":"John Warner Backus"}
    database.add(n1)
    database.add(n2)

    values = database.get({"title":"java"})
    for value in values:
        print(value)

    database.delete({"title":"java"})
    database.delete({"title":"fortran"})

    i = 0

