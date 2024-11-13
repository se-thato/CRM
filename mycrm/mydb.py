
import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = '@THATO53',
)

#prepare cursor object
cursorObject = dataBase.cursor()

#create the database
cursorObject.execute("CREATE DATABASE dynamic")

print("Done! database created successfully")


database = mysql.connector.connect(
    host = "localhost",
    user = "root", 
    passwd = "@THATO53",
    database = "dynamic"

)

cursorObject = database.cursor()

print("connected to 'dynamic' database successfully!")
