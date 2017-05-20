from __future__ import print_function
import re

from datetime import date, datetime, timedelta
import mysql.connector

values=[]


with open  ('save4.txt', 'r') as f:
    for  rec in f:
        a= (rec.split(': ')[1])
        values.append(a)

for word in values:
    print (word)

cnx = mysql.connector.connect(user='root',password = 'root', database='adas')
cursor = cnx.cursor()

query = "INSERT INTO adas VALUES ("

wordLed=len(values)
for i in range(0,wordLed):
    #query = query + "',"
    query = query + values[i]

query = query  + ")"

query = (query.split('}')[0])
query= query+")"

print(query)

cursor.execute(query)


# Make sure data is committed to the database
cnx.commit()
cursor.close()
cnx.close()


