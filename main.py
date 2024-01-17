import mysql.connector

mydb = mysql.connector.connect(
    host="DESKTOP-OTMM446",
    user="admin",
    passwd="admin",
    database="testdb"
)

mycursor = mydb.cursor()

sqlFormula = "INSERT INTO students (name, age) VALUES (%s, %s)"
students = [("Avi", 22),
            ("Bob", 22),
            ("Amanda", 22),
            ("Jacob", 22),
            ("Michelle", 22)]

mycursor.executemany(sqlFormula, students)

mydb.commit()