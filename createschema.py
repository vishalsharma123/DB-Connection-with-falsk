from __future__ import print_function
import re

from datetime import date, datetime, timedelta
import mysql.connector
from mysql.connector import errorcode

cnx = mysql.connector.connect(user='root',password = 'root')
cursor = cnx.cursor()

cursor.execute("""CREATE DATABASE IF NOT EXISTS Testdb3""")
cnx.commit()

cursor.execute("""USE Testdb3""")
cnx.commit()





cursor.execute("""CREATE TABLE IF NOT EXISTS new_adas(
    `Date` varchar(1000) DEFAULT NULL,
    `In-Other` int(11) DEFAULT NULL,
  `In-Satisfied` int(11) DEFAULT NULL,
  `In-Verified` int(10) DEFAULT NULL,
  `Incoming` varchar(100) DEFAULT NULL,
  `Leaf` varchar(100) DEFAULT NULL,
  `ModuleName` varchar(300) DEFAULT NULL,
  `Object Identifier` varchar(1000) DEFAULT NULL,
  `Out-Other` varchar(10) DEFAULT NULL,
  `Out-Satisfied` varchar(100) DEFAULT NULL,
  `Out-Verified` varchar(100) DEFAULT NULL,
  `Outgoing` varchar(100) DEFAULT NULL,
  `ProjectName` varchar(1000) DEFAULT NULL,
  `Req. Status` varchar(300) DEFAULT NULL,
  `Target release` varchar(1000) DEFAULT NULL,
  `TargetList` varchar(1000) DEFAULT NULL,
  `_ASIL_level` varchar(300) DEFAULT NULL,
  `_ImpactedDiscipline` varchar(300) DEFAULT NULL,
  `_ObjectType` varchar(1000) DEFAULT NULL,
  `_ReqLevel` varchar(300) DEFAULT NULL,
  `_ReqStatus` varchar(1000) DEFAULT NULL,
  `_ReqStatusDesign` varchar(1000) DEFAULT NULL,
  `_ReqStatusFuSa` varchar(1000) DEFAULT NULL,
  `_ReqStatusHW` varchar(300) DEFAULT NULL,
  `_ReqStatusMCH` varchar(300) DEFAULT NULL,
  `_ReqStatusSHR` varchar(1000) DEFAULT NULL,
  `_ReqStatusSW` varchar(1000) DEFAULT NULL,
  `_ReqStatusSYS` varchar(300) DEFAULT NULL,
  `_ReqStatusTest` varchar(1000) DEFAULT NULL,
  `_System Functions` varchar(1000) DEFAULT NULL,
  `_Target` varchar(500) DEFAULT NULL,
  `_TestStatus` varchar(500) DEFAULT NULL,
  `_Type` varchar(500) DEFAULT NULL,
  `_TypeSHR` varchar(500) DEFAULT NULL,
  `_VerificationLevel` varchar(200) DEFAULT NULL,
  `url` varchar(1000) DEFAULT NULL)""")
cnx.commit()
cursor.close()
values =[]
rowcount=0;

cnx = mysql.connector.connect(user='root',password = 'root', database='testdb3')
cursor = cnx.cursor()

with open('Ramesh.txt', 'r') as f:
    for rec in f:
        splittedRecord = rec.split(': ')

        if len(values).__eq__(36):
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


# Make sure data is committed to the database
cnx.commit()
cursor.close()
cnx.close()

