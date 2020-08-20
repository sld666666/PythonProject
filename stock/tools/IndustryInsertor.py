import mysql.connector as mc

def initConnector():
    mydb = mc.connect(
        host="localhost",
        user="root",
        passwd="123456",
        database = "stock"
    )

    mycursor = mydb.cursor()
    print(mycursor)

if __name__=='__main__':
    initConnector()
