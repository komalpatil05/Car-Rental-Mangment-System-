import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="mydatabase"
)

if conn.is_connected():
    print("MySQL Connected Successfully")
else:
    print("Connection Failed")
