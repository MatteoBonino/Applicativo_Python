import mysql.connector

mydb = mysql.connector.connect(
    host="DESKTOP-OTMM446",
    user="admin",
    passwd="admin"

)

print(mydb)