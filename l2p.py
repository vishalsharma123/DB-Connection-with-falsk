from __future__ import print_function
from All_modules_ADAS1 import data
import re

from datetime import date, datetime, timedelta
import mysql.connector
from mysql.connector import errorcode

cnx = mysql.connector.connect(user='root',password = '9b83Kk6#')
cursor = cnx.cursor()

dbName='adasapi59'
tabName = 'adas'

colNames=tuple(data[0].keys())

def createDBandTAB(dbName,tabName):

    query1="CREATE DATABASE IF NOT EXISTS {}".format((dbName))
    cursor.execute(query1)

    query2="USE {}".format((dbName))
    cursor.execute(query2)

    query3= """CREATE TABLE IF NOT EXISTS {}(
    `Date` varchar(100) DEFAULT NULL,`In-Other` int(11) DEFAULT NULL,
  `In-Satisfied` int(11) DEFAULT NULL,
  `In-Verified` int(10) DEFAULT NULL,
  `Incoming` varchar(100) DEFAULT NULL,
  `Leaf` varchar(100) DEFAULT NULL,
  `Object Identifier` varchar(500) DEFAULT NULL,
  `Out-Other` varchar(10) DEFAULT NULL,
  `Out-Satisfied` varchar(100) DEFAULT NULL,
  `Out-Verified` varchar(100) DEFAULT NULL,
  `Outgoing` varchar(100) DEFAULT NULL,
  `ProjectName` varchar(500) DEFAULT NULL,
  `Req. Status` varchar(500) DEFAULT NULL,
  `Target release` varchar(1000) DEFAULT NULL,
  `TargetList` varchar(500) DEFAULT NULL,
  `_ASIL_level` varchar(500) DEFAULT NULL,
  `_ImpactedDiscipline` varchar(500) DEFAULT NULL,
  `_ObjectType` varchar(500) DEFAULT NULL,
  `_ReqLevel` varchar(500) DEFAULT NULL,
  `_ReqStatus` varchar(500) DEFAULT NULL,
  `_ReqStatusDesign` varchar(500) DEFAULT NULL,
  `_ReqStatusFuSa` varchar(500) DEFAULT NULL,
  `_ReqStatusHW` varchar(300) DEFAULT NULL,
  `_ReqStatusMCH` varchar(300) DEFAULT NULL,
  `_ReqStatusSHR` varchar(500) DEFAULT NULL,
  `_ReqStatusSW` varchar(500) DEFAULT NULL,
  `_ReqStatusSYS` varchar(300) DEFAULT NULL,
  `_ReqStatusTest` varchar(500) DEFAULT NULL,
  `_System Functions` varchar(500) DEFAULT NULL,
  `_Target` varchar(500) DEFAULT NULL,
  `_TestStatus` varchar(500) DEFAULT NULL,
  `_Type` varchar(500) DEFAULT NULL,
  `_TypeSHR` varchar(500) DEFAULT NULL,
  `_VerificationLevel` varchar(200) DEFAULT NULL,
  `url` varchar(1000) DEFAULT NULL)""".format((tabName))
    cursor.execute(query3)

    cnx.commit()


def add_row(cursor, tabName, rowdict):

    keys=rowdict.keys()
    kt=tuple(keys)
    ks= str(kt)
    columns=ks.replace("'","`")

    values = tuple(rowdict[key] for key in kt)
    vl = list(values)
    for i in range(len(vl)):
        if vl[i] == '':
            vl[i] = 'NULL'
        else:
            vl[i] = vl[i].strip()
    values = tuple(vl)

    sql = "INSERT INTO {} {} VALUES {}".format((tabName), (columns), (values))

    try:
        cursor.execute(sql)
        print ('executed')
    except:
        print (sql)


def addColumn(tabName,colName):
    query = "ALTER TABLE {}".format((tabName))
    query = query + " ADD COLUMN `{}`".format((colName))
    query = query + " varchar(1000)"
    print (query)
    cursor.execute(query)
    print((colName)+ "is added")

def checkIfColExists(dbname, tabName, colName):

    query = "SELECT count(COLUMN_NAME) FROM INFORMATION_SCHEMA.columns WHERE TABLE_NAME = '{}' AND COLUMN_NAME = '{}' and TABLE_SCHEMA ='{}'".format((tabName),(colName),(dbname))
    cursor.execute(query)
    cnt= cursor.fetchall()[0][0]
    if cnt == 1 :
        output= "'{}' is already presented in '{}'".format((colName),(tabName))
        print (output)
    else:
        print (colName)
        addColumn(tabName,str(colName))

if __name__ == "__main__":
    createDBandTAB(dbName,tabName)
    for colName in colNames:
        checkIfColExists(dbName, tabName, colName)

    for row in data:
        add_row(cursor, tabName, row)

    cnx.commit()
    cursor.close()
    cnx.close()