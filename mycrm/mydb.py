import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'theplanetisflat',
)

#prepare cursor object
cursorObject = dataBase.cursor()

#create the database
cursorObject.execute("CREATE DATABASE mycrm")

print("Done! database created successfully")

