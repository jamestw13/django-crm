import mysql.connector

dataBase = mysql.connector.connect(
    host='localhost',
    user = 'root',
    passwd = '6yMIKy1Z0D7H'
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE dcrm")

print("Server started!")