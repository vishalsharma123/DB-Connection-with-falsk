from flask import Flask, render_template, json, request
from flaskext.mysql import MySQL
from flask import Flask
from flask import Markup
from flask import Flask
import csv
import operator

app = Flask(__name__)
mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'adas'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)
conn = mysql.connect()
cursor = conn.cursor()


conn = mysql.connect()
cursor = conn.cursor()

cursor.execute("select _ImpactedDiscipline, count(*) from new_adas group by _ImpactedDiscipline")
data = cursor.fetchall()
x1 =data[0]
print (x1)
a = x1[1]
i =0
j = 0
temp = ""





Target_List1=[i for i in range(a)]
for i in range(a):
    cursor.execute("select _ImpactedDiscipline, count(*) from new_adas group by _ImpactedDiscipline")
    data1 = cursor.fetchall()
    T = x1[i]
    print(T)
    Target_List1[i] = T
    print(T )
    break

