from __future__ import print_function
import re

from datetime import date, datetime, timedelta
import mysql.connector

values =[]
rowcount=0;

cnx = mysql.connector.connect(user='root',password = 'root', database='adas')
cursor = cnx.cursor()

with open('save4.txt', 'r') as f:
    for rec in f:
        splittedRecord = rec.split(': ')

        if len(values).__eq__(35):
            print('true')

            query = "INSERT INTO new_adas VALUES ("

            wordLed = len(values)
            #print(wordLed)
            for i in range(0, wordLed):
                query = query + values[i]

            query = query + ")"

            query = (query.split('}')[0])
            query = query + ")"

            print(query)

            cursor.execute(query)

            values = []
            values.append(splittedRecord[1])
        else:
            values.append(splittedRecord[1])

query = "INSERT INTO new_adas VALUES ("

wordLed = len(values)
#print(wordLed)
for i in range(0, wordLed):
    query = query + values[i]

query = query + ")"

query = (query.split('}')[0])
query = query + ")"

print(query)

cursor.execute(query)

cnx.commit()
cursor.close()
cnx.close()