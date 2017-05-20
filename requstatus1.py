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
data= cursor.fetchall()



cursor.execute("select _ReqStatusSHR, count(*) from new_adas group by _ReqStatusSHR")
data1 = cursor.fetchall()

cursor.execute("select _TypeSHR, count(*) from new_adas group by _TypeSHR")
data2 = cursor.fetchall()

cursor.execute("select count(*) from new_adas")
total = cursor.fetchall()
totalInt = int(total[0][0])

cursor.execute("select distinct TargetList,max(LENGTH(TargetList) - LENGTH(REPLACE(TargetList, ',', ''))) from new_adas ")

data = cursor.fetchall()
x =data[0]
print (x)
a = x[1]
i =0
j = 0
temp = ""

Target_List=[i for i in range(a)]
First_Filter=[i for i in range(a)]
Second_Filter=[i for i in range(a)]
Third_Filter=[i for i in range(a)]
Fourth_Filter=[i for i in range(a)]
Five_Filter=[i for i in range(a)]
Six_Filter=[i for i in range(a)]
Seventh_Filter=[i for i in range(a)]
Eight_Filter =[i for i in range(a)]
Nine_Filter = [i for i in range(a)]
Tenth_Filter = [i for i in range(a)]
Eleventh_filter =[i for i in range(a)]
Twelveth_Filter =[i for i in range(a)]
Therteen_Filter = [i for i in range(a)]
fourteen_Filter = [i for i in range(a)]
fifteen_Filter = [i for i in range(a)]
sixteen_Filter = [i for i in range(a)]
seventeen_Filter = [i for i in range(a)]
Eighteen_Filter = [i for i in range(a)]
nineteen_Filter = [i for i in range(a)]
twenty_Filter = [i for i in range(a)]
twentyone_Filter = [i for i in range(a)]
twentytwo_Filter = [i for i in range(a)]
twentythree_Filter = [i for i in range(a)]
twentyfour_Filter =[i for i in range(a)]
twentyfive_Filter = [i for i in range(a)]
twentysix_Filter = [i for i in range(a)]
twentyseven_Filter=[i for i in range(a)]
twentyeight_Filter=[i for i in range(a)]
twentynine_Filter = [i for i in range(a)]
thirty_Filter=[i for i in range(a)]
thirtyone_Filter=[i for i in range(a)]
thirtytwo_Filter=[i for i in range(a)]
thirtythree_Filter=[i for i in range(a)]
thirtyfour_Filter=[i for i in range(a)]
thirtyfive_Filter = [i for i in range(a)]
thirtysix_Filter = [i for i in range(a)]
thirtyseven_Filter = [i for i in range(a)]
thirtyeight_Filter = [i for i in range(a)]
thirtynine_Filter =[i for i in range(a)]
fourty_Filter = [i for i in range(a)]
fourtyone_Filter = [i for i in range(a)]
fourtytwo_Filter = [i for i in range(a)]
fourtythree_Filter = [i for i in range(a)]
fourtyfour_Filter = [i for i in range(a)]
fourtyfive_Filter = [i for i in range(a)]
fourtysix_Filter = [i for i in range(a)]
fourtyseven_Filter = [i for i in range(a)]

@app.route("/")
def main():

 for i in range(a):
    cursor.execute("select distinct TargetList,substring_index(substring_index(TargetList, ',',%s),',',-1) from new_adas order by length(TargetList) desc;",i+1)
    data1 = cursor.fetchall()
    T =data1[0][1]
    print(T)
    Target_List[i]=T
    #print()
# First filter table
 for j in range(a):
    #print(len(Target_List))
    cursor.execute("select count(*) from new_adas where(_Type = 'Functional Requirement' OR _Type ='Non-functional Requirement') AND (_Target like %s)","%"+Target_List[j])
    data9 = cursor.fetchall()
    first_filter_value = data9[0][0]
    First_Filter[j]=first_filter_value


# Second filter table
 for j in range(a):
    #print(len(Target_List))
    query = """ select count(*) from new_adas where(_Type = 'Functional Requirement' OR _Type ='Non-functional Requirement') AND _Target like '%{}' AND _ImpactedDiscipline like '%{}%'""".format((Target_List[j]),('SW'))
    cursor.execute(query)
    data10 = cursor.fetchall()
    second_filter_value = data10[0][0]
    Second_Filter[j]=second_filter_value
    #print(second_filter_value)
 for j in range(a):
        query = """ select count(*) from new_adas where(_Type = 'Functional Requirement' OR _Type ='Non-functional Requirement') AND _Target like'%{}' AND _ImpactedDiscipline like '%{}%'""".format((Target_List[j]), ('HW'))
        cursor.execute(query)
        data12 = cursor.fetchall()
        third_filter_value = data12[0][0]
        Third_Filter[j] = third_filter_value
        #print(Third_Filter[j])

 for j in range(a):
        query = """ select count(*) from new_adas where(_Type = 'Functional Requirement' OR _Type ='Non-functional Requirement') AND _Target like'%{}' AND _ImpactedDiscipline like '%{}%'""".format(
            (Target_List[j]), ('Mechanical'))
        cursor.execute(query)
        data12 = cursor.fetchall()
        Fourth_filter_value = data12[0][0]
        Fourth_Filter[j] = Fourth_filter_value
        # print(Third_Filter[j])

 for j in range(a):
        query = """ select count(*) from new_adas where(_Type = 'Functional Requirement' OR _Type ='Non-functional Requirement') AND _Target like'{}' AND _ImpactedDiscipline like '{}'""".format(
            (Target_List[j]), ('SW'))
        cursor.execute(query)
        data12 = cursor.fetchall()
        Five_filter_value = data12[0][0]
        Five_Filter[j] = Five_filter_value
        # print(Fourth_Filter[j])

 for j in range(a):
        query = """ select count(*) from new_adas where(_Type = 'Functional Requirement' OR _Type ='Non-functional Requirement') AND _Target like'{}' AND _ImpactedDiscipline like '{}'""".format(
            (Target_List[j]), ('HW'))
        cursor.execute(query)
        data12 = cursor.fetchall()
        Six_filter_value = data12[0][0]
        Six_Filter[j] = Six_filter_value
        # print(Third_Filter[j])

 for j in range(a):
        query = """ select count(*) from new_adas where(_Type = 'Functional Requirement' OR _Type ='Non-functional Requirement') AND _Target like'{}' AND _ImpactedDiscipline like '{}'""".format(
            (Target_List[j]), ('Mechanical'))
        cursor.execute(query)
        data12 = cursor.fetchall()
        Seventh_filter_value = data12[0][0]
        Seventh_Filter[j] = Seventh_filter_value
        # print(Third_Filter[j])

 for j in range(a):
        query = """ select count(*) from new_adas where(_Type = 'Functional Requirement' OR _Type ='Non-functional Requirement') AND _Target like'{}' AND _ReqStatus like '%{}%'""".format(
            (Target_List[j]), ('Init'))
        cursor.execute(query)
        data12 = cursor.fetchall()
        Eight_filter_value = data12[0][0]
        Eight_Filter[j] = Eight_filter_value
        # print(Third_Filter[j])

 for j in range(a):
        query = """ select count(*) from new_adas where(_Type = 'Functional Requirement' OR _Type ='Non-functional Requirement') AND _Target like'{}' AND _ReqStatus like '%{}%'""".format(
            (Target_List[j]), ('In Review'))
        cursor.execute(query)
        data12 = cursor.fetchall()
        Nine_filter_value = data12[0][0]
        Nine_Filter[j] = Nine_filter_value
        #print(Third_Filter[j])

 for j in range(a):
        query = """ select count(*) from new_adas where(_Type = 'Functional Requirement' OR _Type ='Non-functional Requirement') AND _Target like'{}' AND _ReqStatus like '%{}%'""".format(
            (Target_List[j]), ('To_be_clarified'))
        cursor.execute(query)
        data12 = cursor.fetchall()
        Tenth_filter_value = data12[0][0]
        Tenth_Filter[j] = Tenth_filter_value
        # print(Third_Filter[j])

 for j in range(a):
        query = """ select count(*) from new_adas where(_Type = 'Functional Requirement' OR _Type ='Non-functional Requirement') AND _Target like'{}' AND _ReqStatus like '%{}%'""".format(
            (Target_List[j]), ('Approved'))
        cursor.execute(query)
        data12 = cursor.fetchall()
        Eleventh_filter_value = data12[0][0]
        Eleventh_filter[j] = Eleventh_filter_value
        # print(Third_Filter[j])

 for j in range(a):
        query = """ select count(*) from new_adas where(_Type = 'Functional Requirement' OR _Type ='Non-functional Requirement') AND _Target like'{}' AND _ReqStatus like '%{}%'""".format(
            (Target_List[j]), ('Obsolete'))
        cursor.execute(query)
        data12 = cursor.fetchall()
        Twelveth_filter_value = data12[0][0]
        Twelveth_Filter[j] = Twelveth_filter_value
        # print(Third_Filter[j])

 for j in range(a):
        query = """ select count(*) from new_adas where(_Type = 'Functional Requirement' OR _Type ='Non-functional Requirement') AND _Target like'{}' AND _ReqStatus like '%{}%'""".format(
            (Target_List[j]), ('Not applicable'))
        cursor.execute(query)
        data12 = cursor.fetchall()
        Therteen_Filter_value = data12[0][0]
        Therteen_Filter[j] = Therteen_Filter_value
        # print(Third_Filter[j])


#filter number $04
 for j in range(a):
        query = """ select count(*) from new_adas where(_Type = 'Functional Requirement' OR _Type ='Non-functional Requirement') AND _Target like'{}' AND _ReqStatusSW like  '%{}%'""".format(
            (Target_List[j]), ('In Review'))
        cursor.execute(query)
        data12 = cursor.fetchall()
        fourteen_filter_value = data12[0][0]
        fourteen_Filter[j] = fourteen_filter_value
        # print(Third_Filter[j])

 for j in range(a):
        query = """ select count(*) from new_adas where(_Type = 'Functional Requirement' OR _Type ='Non-functional Requirement') AND _Target like'{}' AND _ReqStatusSW like  '%{}%'""".format(
            (Target_List[j]), ('Approved'))
        cursor.execute(query)
        data12 = cursor.fetchall()
        fifteen_filter_value = data12[0][0]
        fifteen_Filter[j] = fifteen_filter_value
        #print(Third_Filter[j])

 for j in range(a):
        query = """ select count(*) from new_adas where(_Type = 'Functional Requirement' OR _Type ='Non-functional Requirement') AND _Target like'{}' AND _ReqStatusSW like  '%{}%'""".format(
            (Target_List[j]), ('To_be_clarified'))
        cursor.execute(query)
        data12 = cursor.fetchall()
        sixteen_filter_value = data12[0][0]
        sixteen_Filter[j] = sixteen_filter_value
        #print(Third_Filter[j])

 for j in range(a):
        query = """ select count(*) from new_adas where(_Type = 'Functional Requirement' OR _Type ='Non-functional Requirement') AND _Target like'{}' AND _ReqStatusSW like  '%{}%'""".format(
            (Target_List[j]), ('Not applicable'))
        cursor.execute(query)
        data12 = cursor.fetchall()
        seventeen_filter_value = data12[0][0]
        seventeen_Filter[j] = seventeen_filter_value
        #print(Third_Filter[j])

 for j in range(a):
        query = """ select count(*) from new_adas where(_Type = 'Functional Requirement' OR _Type ='Non-functional Requirement') AND _Target like'{}' AND _ReqStatusTest like  '%{}%'""".format(
            (Target_List[j]), ('In Review'))
        cursor.execute(query)
        data12 = cursor.fetchall()
        Eighteen_filter_value = data12[0][0]
        Eighteen_Filter[j] = Eighteen_filter_value
 for j in range(a):
     query = """ select count(*) from new_adas where(_Type = 'Functional Requirement' OR _Type ='Non-functional Requirement') AND _Target like'{}' AND _ReqStatusTest like  '%{}%'""".format(
         (Target_List[j]), ('Approved'))
     cursor.execute(query)
     data12 = cursor.fetchall()
     nineteen_filter_value = data12[0][0]
     nineteen_Filter[j] = nineteen_filter_value
     # print(Third_Filter[j])

 for j in range(a):
     query = """ select count(*) from new_adas where(_Type = 'Functional Requirement' OR _Type ='Non-functional Requirement') AND _Target like'{}' AND _ReqStatusTest like  '%{}%'""".format(
         (Target_List[j]), ('To_be_clarified'))
     cursor.execute(query)
     data12 = cursor.fetchall()
     twenty_filter_value = data12[0][0]
     twenty_Filter[j] = twenty_filter_value
     # print(Third_Filter[j])

 for j in range(a):
     query = """ select count(*) from new_adas where(_Type = 'Functional Requirement' OR _Type ='Non-functional Requirement') AND _Target like'{}' AND _ReqStatusTest like  '%{}%'""".format(
         (Target_List[j]), ('Not applicable'))
     cursor.execute(query)
     data12 = cursor.fetchall()
     twentyone_filter_value = data12[0][0]
     twentyone_Filter[j] = twentyone_filter_value
 for j in range(a):
         query = """ select count(*) from new_adas where(_Type = 'Functional Requirement' OR _Type ='Non-functional Requirement') AND _Target like'{}' AND _ReqStatusFuSa like  '%{}%'""".format(
             (Target_List[j]), ('In Review'))
         cursor.execute(query)
         data12 = cursor.fetchall()
         twentytwo_filter_value = data12[0][0]
         twentytwo_Filter[j] = twentytwo_filter_value
 for j in range(a):
         query = """ select count(*) from new_adas where(_Type = 'Functional Requirement' OR _Type ='Non-functional Requirement') AND _Target like'{}' AND _ReqStatusFuSa like  '%{}%'""".format(
             (Target_List[j]), ('Approved'))
         cursor.execute(query)
         data12 = cursor.fetchall()
         twentythree_filter_value = data12[0][0]
         twentythree_Filter[j] = twentythree_filter_value
         # print(Third_Filter[j])

 for j in range(a):
         query = """ select count(*) from new_adas where(_Type = 'Functional Requirement' OR _Type ='Non-functional Requirement') AND _Target like'{}' AND _ReqStatusFuSa like  '%{}%'""".format(
             (Target_List[j]), ('To_be_clarified'))
         cursor.execute(query)
         data12 = cursor.fetchall()
         twentyfour_filter_value = data12[0][0]
         twentyfour_Filter[j] = twentyfour_filter_value
         # print(Third_Filter[j])

 for j in range(a):
         query = """ select count(*) from new_adas where(_Type = 'Functional Requirement' OR _Type ='Non-functional Requirement') AND _Target like'{}' AND _ReqStatusFuSa like  '%{}%'""".format(
         (Target_List[j]), ('Not applicable'))
         cursor.execute(query)
         data12 = cursor.fetchall()
         twentyfive_filter_value = data12[0][0]
         twentyfive_Filter[j] = twentyfive_filter_value
 for j in range(a):
        query = """ select count(*) from new_adas where(_Type = 'Functional Requirement' OR _Type ='Non-functional Requirement') AND _Target like'{}' AND _ReqStatusHW like  '%{}%'""".format(
            (Target_List[j]), ('In Review'))
        cursor.execute(query)
        data12 = cursor.fetchall()
        twentysix_filter_value = data12[0][0]
        twentysix_Filter[j] = twentysix_filter_value
        print(twentysix_Filter[j])

 for j in range(a):
        query = """ select count(*) from new_adas where(_Type = 'Functional Requirement' OR _Type ='Non-functional Requirement') AND _Target like'{}' AND _ReqStatusHW like  '%{}%'""".format(
            (Target_List[j]), ('Approved'))
        cursor.execute(query)
        data12 = cursor.fetchall()
        twentyseven_filter_value = data12[0][0]
        twentyseven_Filter[j] = twentyseven_filter_value
        #print(Third_Filter[j])

 for j in range(a):
        query = """ select count(*) from new_adas where(_Type = 'Functional Requirement' OR _Type ='Non-functional Requirement') AND _Target like'{}' AND _ReqStatusHW like  '%{}%'""".format(
        (Target_List[j]), ('To_be_clarified'))
        cursor.execute(query)
        data12 = cursor.fetchall()
        twentyeight_filter_value = data12[0][0]
        twentyeight_Filter[j] = twentyeight_filter_value
        #print(Third_Filter[j])

 for j in range(a):
        query = """ select count(*) from new_adas where(_Type = 'Functional Requirement' OR _Type ='Non-functional Requirement') AND _Target like'{}' AND _ReqStatusHW like  '%{}%'""".format(
        (Target_List[j]), ('Not applicable'))
        cursor.execute(query)
        data12 = cursor.fetchall()
        twentynine_filter_value = data12[0][0]
        twentynine_Filter[j] = twentynine_filter_value
        #print(Third_Filter[j])
 for j in range(a):
        query = """ select count(*) from new_adas where(_Type = 'Functional Requirement' OR _Type ='Non-functional Requirement') AND _Target like'{}' AND _ReqStatusMCH like  '%{}%'""".format(
            (Target_List[j]), ('In Review'))
        cursor.execute(query)
        data12 = cursor.fetchall()
        thirty_filter_value = data12[0][0]
        thirty_Filter[j] = thirty_filter_value
        #print(twentysix_Filter[j])

 for j in range(a):
        query = """ select count(*) from new_adas where(_Type = 'Functional Requirement' OR _Type ='Non-functional Requirement') AND _Target like'{}' AND _ReqStatusMCH like  '%{}%'""".format(
            (Target_List[j]), ('Approved'))
        cursor.execute(query)
        data12 = cursor.fetchall()
        thirtyone_filter_value = data12[0][0]
        thirtyone_Filter[j] = thirtyone_filter_value
        #print(Third_Filter[j])

 for j in range(a):
        query = """ select count(*) from new_adas where(_Type = 'Functional Requirement' OR _Type ='Non-functional Requirement') AND _Target like'{}' AND _ReqStatusMCH like  '%{}%'""".format(
        (Target_List[j]), ('To_be_clarified'))
        cursor.execute(query)
        data12 = cursor.fetchall()
        thirtytwo_filter_value = data12[0][0]
        thirtytwo_Filter[j] = thirtytwo_filter_value
        #print(Third_Filter[j])

 for j in range(a):
        query = """ select count(*) from new_adas where(_Type = 'Functional Requirement' OR _Type ='Non-functional Requirement') AND _Target like'{}' AND _ReqStatusMCH like  '%{}%'""".format(
        (Target_List[j]), ('Not applicable'))
        cursor.execute(query)
        data12 = cursor.fetchall()
        thirtythree_filter_value = data12[0][0]
        thirtythree_Filter[j] = thirtythree_filter_value
        #print(Third_Filter[j])

 for j in range(a):
        query = """ select count(*) from new_adas where(_Type = 'Functional Requirement' OR _Type ='Non-functional Requirement') AND _Target like'{}' AND _ReqStatusSYS like  '%{}%'""".format(
            (Target_List[j]), ('In Review'))
        cursor.execute(query)
        data12 = cursor.fetchall()
        thirtyfour_filter_value = data12[0][0]
        thirtyfour_Filter[j] = thirtyfour_filter_value
        #print(twentysix_Filter[j])

 for j in range(a):
        query = """ select count(*) from new_adas where(_Type = 'Functional Requirement' OR _Type ='Non-functional Requirement') AND _Target like'{}' AND _ReqStatusSYS like  '%{}%'""".format(
            (Target_List[j]), ('Approved'))
        cursor.execute(query)
        data12 = cursor.fetchall()
        thirtyfive_filter_value = data12[0][0]
        thirtyfive_Filter[j] = thirtyfive_filter_value
        #print(Third_Filter[j])

 for j in range(a):
        query = """ select count(*) from new_adas where(_Type = 'Functional Requirement' OR _Type ='Non-functional Requirement') AND _Target like'{}' AND _ReqStatusSYS like  '%{}%'""".format(
        (Target_List[j]), ('To_be_clarified'))
        cursor.execute(query)
        data12 = cursor.fetchall()
        thirtysix_filter_value = data12[0][0]
        thirtysix_Filter[j] = thirtysix_filter_value
        #print(Third_Filter[j])

 for j in range(a):
        query = """ select count(*) from new_adas where(_Type = 'Functional Requirement' OR _Type ='Non-functional Requirement') AND _Target like'{}' AND _ReqStatusSYS like  '%{}%'""".format(
        (Target_List[j]), ('Not applicable'))
        cursor.execute(query)
        data12 = cursor.fetchall()
        thirtyseven_filter_value = data12[0][0]
        thirtyseven_Filter[j] = thirtyseven_filter_value
        #print(Third_Filter[j])
 cursor.execute("select _ImpactedDiscipline, count(*) from new_adas group by _ImpactedDiscipline")
 data = cursor.fetchall()

 cursor.execute("select _ReqStatusSHR, count(*) from new_adas group by _ReqStatusSHR")
 data1 = cursor.fetchall()

 cursor.execute("select _TypeSHR, count(*) from new_adas group by _TypeSHR")
 data2 = cursor.fetchall()

 cursor.execute("select count(*) from new_adas")
 total = cursor.fetchall()
 hiddenVariable=[True,False,False,False,False]

 hiddenVariable = [True, False, False, False, False]

 z = tuple(map(operator.add, Second_Filter, Third_Filter))
 y = tuple(map(operator.add, z, Fourth_Filter))
 k = list(y)
 PL = sum(k)

 c = tuple(map(operator.add, fourteen_Filter, fifteen_Filter))
 d = tuple(map(operator.add, c, sixteen_Filter))
 total_for_sw = tuple(map(operator.add, d, seventeen_Filter))
 p1 = list(total_for_sw)
 PD = sum(p1)

 # print(total_for_sw)
 KP = tuple(map(operator.add, Five_Filter, Six_Filter))
 KP1 = tuple(map(operator.add, KP, Seventh_Filter))
 Q = list(KP1)
 PF = sum(Q)
 CP = tuple(map(operator.add, Eight_Filter, Nine_Filter))
 CP1 = tuple(map(operator.add, CP, Tenth_Filter))
 CP2 = tuple(map(operator.add, CP1, Eleventh_filter))
 CP3 = tuple(map(operator.add, CP2, Twelveth_Filter))
 CP4 = tuple(map(operator.add, CP3, Therteen_Filter))
 R = list(CP4)
 PR = sum(R)
 R_S_Test = tuple(map(operator.add, Eighteen_Filter, nineteen_Filter))
 R_S_Test1 = tuple(map(operator.add, R_S_Test, twenty_Filter))
 total_for_Reqests = tuple(map(operator.add, R_S_Test1, twentyone_Filter))
 p2 = list(total_for_Reqests)
 PK = sum(p2)
 # print (total_for_Reqests )
 R_S_Test_Fusa = tuple(map(operator.add, twentytwo_Filter, twentythree_Filter))
 R_S_Test_Fusa1 = tuple(map(operator.add, R_S_Test_Fusa, twentyfour_Filter))
 total_for_Reqests_Fusa = tuple(map(operator.add, R_S_Test_Fusa1, twentyfive_Filter))
 # print (total_for_Reqests_Fusa )
 p3 = list(total_for_Reqests_Fusa)
 PC = sum(p3)
 R_S_Test_HW = tuple(map(operator.add, twentysix_Filter, twentyseven_Filter))
 R_S_Test_HW1 = tuple(map(operator.add, R_S_Test_HW, twentyeight_Filter))
 total_for_Reqests_HW = tuple(map(operator.add, R_S_Test_HW1, twentynine_Filter))
 # print (total_for_Reqests_HW )
 p4 = list(total_for_Reqests_HW)
 PE = sum(p4)
 R_S_Test_MECH = tuple(map(operator.add, thirty_Filter, thirtyone_Filter))
 R_S_Test_MECH1 = tuple(map(operator.add, R_S_Test_MECH, thirtytwo_Filter))
 total_for_Reqests_MECH = tuple(map(operator.add, R_S_Test_MECH1, thirtythree_Filter))
 # print (total_for_Reqests+_+++)
 p5 = list(total_for_Reqests_MECH)
 PX = sum(p5)
 R_S_Test_SYS = tuple(map(operator.add, thirtyfour_Filter, thirtyfive_Filter))
 R_S_Test_SYS1 = tuple(map(operator.add, R_S_Test_SYS, thirtysix_Filter))
 total_for_Reqests_SYS2 = tuple(map(operator.add, R_S_Test_SYS1, thirtyseven_Filter))
 # print (total_for_Reqests_HW )
 p6 = list(total_for_Reqests_SYS2)
 PY = sum(p6)
 _System_F = tuple(map(operator.add, thirtyeight_Filter, thirtynine_Filter))
 _System_F1 = tuple(map(operator.add, _System_F, fourty_Filter))
 _System_F2 = tuple(map(operator.add, _System_F1, fourtyone_Filter))
 _System_F3 = tuple(map(operator.add, _System_F2, fourtytwo_Filter))
 _System_F4 = tuple(map(operator.add, _System_F3, fourtythree_Filter))
 _System_F5 = tuple(map(operator.add, _System_F4, fourtyfour_Filter))
 _System_F6 = tuple(map(operator.add, _System_F5, fourtyfive_Filter))
 _System_F7 = tuple(map(operator.add, _System_F6, fourtysix_Filter))
 _System_F8 = tuple(map(operator.add, _System_F7, fourtyseven_Filter))
 PLK = list(_System_F8)
 PLK1 = sum(PLK)

 return render_template('Filter.html', data=data, data1=data1, data2=data2, total=total, targetList=Target_List,
                        firstFilter=First_Filter, Second_Filter=Second_Filter, Third_Filter=Third_Filter,
                        Fourth_Filter=Fourth_Filter, Five_Filter=Five_Filter, Six_Filter=Six_Filter,
                        Seventh_Filter=Seventh_Filter, Eight_Filter=Eight_Filter, Nine_Filter=Nine_Filter,
                        Tenth_Filter=Tenth_Filter, Eleventh_filter=Eleventh_filter,
                        Twelveth_Filter=Twelveth_Filter, Therteen_Filter=Therteen_Filter,
                        fourteen_Filter=fourteen_Filter, fifteen_Filter=fifteen_Filter, sixteen_Filter=sixteen_Filter,
                        seventeen_Filter=seventeen_Filter, Eighteen_Filter=Eighteen_Filter, total_for_sw=p1,
                        nineteen_Filter=nineteen_Filter, twenty_Filter=twenty_Filter, twentyone_Filter=twentyone_Filter,
                        total_for_Reqests=p2, twentytwo_Filter=twentytwo_Filter, twentythree_Filter=twentythree_Filter,
                        twentyfour_Filter=twentyfour_Filter, twentyfive_Filter=twentyfive_Filter,
                        total_for_Reqests_Fusa=p3, y=k, hiddenVariable=hiddenVariable,
                        twentysix_Filter=twentysix_Filter, twentyseven_Filter=twentyseven_Filter,
                        twentyeight_Filter=twentyeight_Filter, twentynine_Filter=twentynine_Filter,
                        total_for_Reqests_HW=p4,
                        thirty_Filter=thirty_Filter, thirtyone_Filter=thirtyone_Filter,
                        thirtytwo_Filter=thirtytwo_Filter, thirtythree_Filter=thirtythree_Filter,
                        total_for_Reqests_MECH=p5,
                        thirtyfour_Filter=thirtyfour_Filter, thirtyfive_Filter=thirtyfive_Filter,
                        thirtysix_Filter=thirtysix_Filter, thirtyseven_Filter=thirtyseven_Filter,
                        total_for_Reqests_SYS2=p6,
                        thirtyeight_Filter=thirtyeight_Filter, thirtynine_Filter=thirtynine_Filter,
                        fourty_Filter=fourty_Filter, fourtyone_Filter=fourtyone_Filter,
                        fourtytwo_Filter=fourtytwo_Filter, fourtythree_Filter=fourtythree_Filter, Q=Q, R=R, PL=PL,
                        PD=PD, PF=PF, PR=PR, PK=PK, PC=PC, PE=PE, PX=PX, PY=PY, totalInt=totalInt,
                        fourtyfour_Filter=fourtyfour_Filter, fourtyfive_Filter=fourtyfive_Filter,
                        fourtysix_Filter=fourtysix_Filter,
                        fourtyseven_Filter=fourtyseven_Filter, _System_F8=_System_F8, PLK=PLK, PLK1=PLK1)


if __name__ == "__main__":
    app.run(debug=True, port=5002)



# for j in range(a):
#
#     query = """ select count(*) from new_adas where(_Type = 'Functional Requirement' OR _Type ='Non-functional Requirement') AND _Target like'%{}' AND _ImpactedDiscipline like '%{}%'""".format((Target_List[j]),('HW'))
#     cursor.execute(query)
#     data12 = cursor.fetchall()
#     third_filter_value = data12[0][0]
#     Third_Filter[j]=third_filter_value
#     print(Third_Filter[j])
#
# for j in range(a):
#
#     query = """ select count(*) from new_adas where(_Type = 'Functional Requirement' OR _Type ='Non-functional Requirement') AND _Target like'%{}' AND _ImpactedDiscipline like '%{}%'""".format((Target_List[j]),('Mechanical'))
#     cursor.execute(query)
#     data12 = cursor.fetchall()
#     third_filter_value = data12[0][0]
#     Third_Filter[j]=third_filter_value
#     print(Third_Filter[j])
#
#
#
# for j in range(a):
#
#     query = """ select count(*) from new_adas where(_Type = 'Functional Requirement' OR _Type ='Non-functional Requirement') AND _Target like'{}' AND _ImpactedDiscipline like '{}'""".format((Target_List[j]),('SW'))
#     cursor.execute(query)
#     data12 = cursor.fetchall()
#     third_filter_value = data12[0][0]
#     Fourth_Filter[j]=third_filter_value
#     print(Fourth_Filter[j])
#
# for j in range(a):
#
#     query = """ select count(*) from new_adas where(_Type = 'Functional Requirement' OR _Type ='Non-functional Requirement') AND _Target like'{}' AND _ImpactedDiscipline like '{}'""".format((Target_List[j]),('HW'))
#     cursor.execute(query)
#     data12 = cursor.fetchall()
#     third_filter_value = data12[0][0]
#     Third_Filter[j]=third_filter_value
#     print(Third_Filter[j])
#
# for j in range(a):
#
#     query = """ select count(*) from new_adas where(_Type = 'Functional Requirement' OR _Type ='Non-functional Requirement') AND _Target like'{}' AND _ImpactedDiscipline like '{}'""".format((Target_List[j]),('Mechanical'))
#     cursor.execute(query)
#     data12 = cursor.fetchall()
#     third_filter_value = data12[0][0]
#     Third_Filter[j]=third_filter_value
#     print(Third_Filter[j])

# for j in range(a):
#
#     query = """ select count(*) from new_adas where(_Type = 'Functional Requirement' OR _Type ='Non-functional Requirement') AND _Target like'{}' AND _ReqStatus like '%{}%'""".format((Target_List[j]),('Init'))
#     cursor.execute(query)
#     data12 = cursor.fetchall()
#     third_filter_value = data12[0][0]
#     Third_Filter[j]=third_filter_value
#     print(Third_Filter[j])
# for j in range(a):
#
#     query = """ select count(*) from adas where(_Type = 'Functional Requirement' OR _Type ='Non-functional Requirement') AND _Target like'{}' AND _ReqStatus like '%{}%'""".format((Target_List[j]),('In Review'))
#     cursor.execute(query)
#     data12 = cursor.fetchall()
#     third_filter_value = data12[0][0]
#     Third_Filter[j]=third_filter_value
#     print(Third_Filter[j])

# for j in range(a):
#
#     query = """ select count(*) from adas where(_Type = 'Functional Requirement' OR _Type ='Non-functional Requirement') AND _Target like'{}' AND _ReqStatus like '%{}%'""".format((Target_List[j]),('To_be_clarified'))
#     cursor.execute(query)
#     data12 = cursor.fetchall()
#     third_filter_value = data12[0][0]
#     Third_Filter[j]=third_filter_value
#     # print(Third_Filter[j])
#
#
# for j in range(a):
#
#     query = """ select count(*) from adas where(_Type = 'Functional Requirement' OR _Type ='Non-functional Requirement') AND _Target like'{}' AND _ReqStatus like '%{}%'""".format((Target_List[j]),('Approved'))
#     cursor.execute(query)
#     data12 = cursor.fetchall()
#     third_filter_value = data12[0][0]
#     Third_Filter[j]=third_filter_value
#     #print(Third_Filter[j])
#
# for j in range(a):
#
#     query = """ select count(*) from adas where(_Type = 'Functional Requirement' OR _Type ='Non-functional Requirement') AND _Target like'{}' AND _ReqStatus like '%{}%'""".format((Target_List[j]),('Obsolete'))
#     cursor.execute(query)
#     data12 = cursor.fetchall()
#     third_filter_value = data12[0][0]
#     Third_Filter[j]=third_filter_value
#     # print(Third_Filter[j])
#
#
# for j in range(a):
#
#     query = """ select count(*) from adas where(_Type = 'Functional Requirement' OR _Type ='Non-functional Requirement') AND _Target like'{}' AND _ReqStatus like '%{}%'""".format((Target_List[j]),('Not applicable'))
#     cursor.execute(query)
#     data12 = cursor.fetchall()
#     third_filter_value = data12[0][0]
#     Third_Filter[j]=third_filter_value
#     # print(Third_Filter[j])
#
#
#
#
# for j in range(a):
#
#     query = """ select count(*) from adas where(_Type = 'Functional Requirement' OR _Type ='Non-functional Requirement') AND _Target like'{}' AND _ReqStatusSW like  '%{}%'""".format((Target_List[j]),('In Review'))
#     cursor.execute(query)
#     data12 = cursor.fetchall()
#     third_filter_value = data12[0][0]
#     Third_Filter[j]=third_filter_value
#     # print(Third_Filter[j])
#
# for j in range(a):
#
#     query = """ select count(*) from adas where(_Type = 'Functional Requirement' OR _Type ='Non-functional Requirement') AND _Target like'{}' AND _ReqStatusSW like  '%{}%'""".format((Target_List[j]),('Approved'))
#     cursor.execute(query)
#     data12 = cursor.fetchall()
#     third_filter_value = data12[0][0]
#     Third_Filter[j]=third_filter_value
#     print(Third_Filter[j])
#
# for j in range(a):
#
#     query = """ select count(*) from adas where(_Type = 'Functional Requirement' OR _Type ='Non-functional Requirement') AND _Target like'{}' AND _ReqStatusSW like  '%{}%'""".format((Target_List[j]),('To_be_clarified'))
#     cursor.execute(query)
#     data12 = cursor.fetchall()
#     third_filter_value = data12[0][0]
#     Third_Filter[j]=third_filter_value
#     print(Third_Filter[j])
#
# for j in range(a):
#
#     query = """ select count(*) from adas where(_Type = 'Functional Requirement' OR _Type ='Non-functional Requirement') AND _Target like'{}' AND _ReqStatusSW like  '%{}%'""".format((Target_List[j]),('Not applicable'))
#     cursor.execute(query)
#     data12 = cursor.fetchall()
#     third_filter_value = data12[0][0]
#     Third_Filter[j]=third_filter_value
#     print(Third_Filter[j])
#
# for j in range(a):
#
#     query = """ select count(*) from adas where(_Type = 'Functional Requirement' OR _Type ='Non-functional Requirement') AND _Target like'{}' AND _ReqStatusSW like  '%{}%'""".format((Target_List[j]),('Not applicable'))
#     cursor.execute(query)
#     data12 = cursor.fetchall()
#     third_filter_value = data12[0][0]
#     Third_Filter[j]=third_filter_value
#     print(Third_Filter[j])


#totalcount done in html page

