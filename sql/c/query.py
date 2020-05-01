import mysql.connector
from mysql.connector import Error

connection = None
try:
    connection = mysql.connector.connect(
        host="localhost",
        database="BDAUTOBUSES",
        user="root",
        password="889927"
    )
except Error as e:
    print("Something did not go as planned", e)

print(connection)
if connection != None:
    while True:
        a = input("Inserte un código de trayecto (q to quit): ")
        if a == 'q':
            break
        print("Los billetes encontrados con ese código de trayecto son:")

        cursor = connection.cursor()
        cursor.execute("select * from BILLETES where CODTRAY='%s'" % (a))
        records = cursor.fetchall()

        for record in records:
            for elem in record:
               print(elem, end='\t')
            print()

    connection.close()


