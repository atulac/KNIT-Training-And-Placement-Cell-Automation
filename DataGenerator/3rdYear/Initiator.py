from collections import defaultdict
from prettytable import PrettyTable
import ThirdYear
import Range
import URL
import MySQLdb

Details=defaultdict(lambda:defaultdict(lambda:'-'))
Branch_Switchers=defaultdict(lambda:defaultdict(lambda:'-'))
UFM=defaultdict(lambda:"")

inputdata=open('InputFile.txt','r')

t=int(inputdata.readline().strip())
print "Number of Operations: "+str(t)+"\n"

db = MySQLdb.connect("localhost","root","","THIRD_YEAR")

if (db):
    print "Connection successful"
else:
    print "Connection Unsuccessful"

cursor = db.cursor()

cursor.execute("DROP TABLE IF EXISTS DETAILED,PRECISE,BRANCH_CHANGERS,GRADE_STATUS,UFM")

sql = """CREATE TABLE DETAILED(
         ROLL INT(10),
         NAME  CHAR(100),
         FATHER_NAME  CHAR(100),
         SEM1 INT(10),
         SEM2 INT(10),
         PENDING1 CHAR(100),
         STATUS1 CHAR(100),
         SEM1_CO INT(10),
         SEM2_CO INT(10),
         PENDING1_CO CHAR(100),
         STATUS1_CO CHAR(100),
         SEM3 INT(10),
         SEM4 INT(10),
         PENDING2 CHAR(100),
         STATUS2 CHAR(100),
         SEM3_CO INT(10),
         SEM4_CO INT(10),
         PENDING2_CO CHAR(100),
         STATUS2_CO CHAR(100),
         SEM5 INT(10),
         SEM6 INT(10),
         PENDING3 CHAR(100),
         STATUS3 CHAR(100)
         )"""

cursor.execute(sql)

sql = """CREATE TABLE GRADE_STATUS(
         ROLL INT(10),
         NAME  CHAR(100),
         STATUS1 CHAR(100),
         STATUS1_CO CHAR(100),
         STATUS2 CHAR(100),
         STATUS2_CO CHAR(100),
         STATUS3 CHAR(100)
         )"""
cursor.execute(sql)

sql = """CREATE TABLE BRANCH_CHANGERS(
         ROLL INT(10),
         NAME  CHAR(100),
         FROM_BRANCH CHAR(100),
         TO_BRANCH CHAR(100)
         )"""

cursor.execute(sql)

sql="""CREATE TABLE UFM(
       SEM CHAR(100),
       ROLLS CHAR(100)
       )"""

cursor.execute(sql)


for i in range(t):
    branch=inputdata.readline().strip()
    year=int(inputdata.readline())
    if year==3:
        ThirdYear.execute(Details,branch,Branch_Switchers,UFM)

Detailed=PrettyTable(["ROLL","NAME","FATHER_NAME","SEM1","SEM2","PENDING1","STATUS1","SEM1_CO","SEM2_CO","PENDING1_CO","STATUS1_CO","SEM3","SEM4",
               "PENDING2","STATUS2","SEM3_CO","SEM4_CO","PENDING2_CO","STATUS2_CO","SEM5","SEM6","PENDING3","STATUS3"])

bswitch=PrettyTable(["ROLL","NAME","FROM BRANCH","TO BRANCH"])

grade_status=PrettyTable(["ROLL","NAME","STATUS1","STATUS1_CO","STATUS2","STATUS2_CO","STATUS3"])

ufm_table=PrettyTable(["SEMESTER","ROLL NUMBERS"])

li=Details.keys()
li.sort()
for ROLL in li:
    Detailed.add_row([Details[ROLL]["ROLL"],Details[ROLL]['NAME'],Details[ROLL]["FATHER's NAME"],Details[ROLL]["SEM1"],Details[ROLL]["SEM2"],Details[ROLL]["PENDING1"],
                   Details[ROLL]["STATUS1"],Details[ROLL]["SEM1_CO"],Details[ROLL]["SEM2_CO"],Details[ROLL]["PENDING1_CO"],Details[ROLL]["STATUS1_CO"],Details[ROLL]["SEM3"],
                   Details[ROLL]["SEM4"],Details[ROLL]["PENDING2"],Details[ROLL]["STATUS2"],Details[ROLL]["SEM3_CO"],Details[ROLL]["SEM4_CO"],Details[ROLL]["PENDING2_CO"],
                   Details[ROLL]["STATUS2_CO"],Details[ROLL]["SEM5"],Details[ROLL]["SEM6"],Details[ROLL]["PENDING3"],Details[ROLL]["STATUS3"]])


    cursor.execute("""INSERT INTO DETAILED(ROLL,NAME,FATHER_NAME,SEM1,SEM2,PENDING1,STATUS1,SEM1_CO,SEM2_CO,PENDING1_CO,STATUS1_CO,SEM3,SEM4,PENDING2,STATUS2,
                   SEM3_CO,SEM4_CO,PENDING2_CO,STATUS2_CO,SEM5,SEM6,PENDING3,STATUS3)
                   VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
                   
                   ,(Details[ROLL]["ROLL"],Details[ROLL]['NAME'],Details[ROLL]["FATHER's NAME"],Details[ROLL]["SEM1"],Details[ROLL]["SEM2"],Details[ROLL]["PENDING1"],
                   Details[ROLL]["STATUS1"],Details[ROLL]["SEM1_CO"],Details[ROLL]["SEM2_CO"],Details[ROLL]["PENDING1_CO"],Details[ROLL]["STATUS1_CO"],Details[ROLL]["SEM3"],
                   Details[ROLL]["SEM4"],Details[ROLL]["PENDING2"],Details[ROLL]["STATUS2"],Details[ROLL]["SEM3_CO"],Details[ROLL]["SEM4_CO"],Details[ROLL]["PENDING2_CO"],
                   Details[ROLL]["STATUS2_CO"],Details[ROLL]["SEM5"],Details[ROLL]["SEM6"],Details[ROLL]["PENDING3"],Details[ROLL]["STATUS3"]))


    grade_status.add_row([Details[ROLL]["ROLL"],Details[ROLL]["NAME"],Details[ROLL]["STATUS1"],Details[ROLL]["STATUS1_CO"],
                   Details[ROLL]["STATUS2"],Details[ROLL]["STATUS2_CO"],Details[ROLL]["STATUS3"]])

    cursor.execute("""INSERT INTO GRADE_STATUS(ROLL,NAME,STATUS1,STATUS1_CO,STATUS2,STATUS2_CO,STATUS3)
                   VALUES(%s,%s,%s,%s,%s,%s,%s)"""
                   ,(Details[ROLL]["ROLL"],Details[ROLL]["NAME"],Details[ROLL]["STATUS1"],Details[ROLL]["STATUS1_CO"],
                   Details[ROLL]["STATUS2"],Details[ROLL]["STATUS2_CO"],Details[ROLL]["STATUS3"]))


print "Branch_Switchers"""
for ROLL in Branch_Switchers.keys():
    bswitch.add_row([Branch_Switchers[ROLL]["ROLL"],Branch_Switchers[ROLL]["NAME"],Branch_Switchers[ROLL]["FROM_BRANCH"],Branch_Switchers[ROLL]["TO_BRANCH"]])

    cursor.execute("""INSERT INTO BRANCH_CHANGERS(ROLL,NAME,FROM_BRANCH,TO_BRANCH)
                   VALUES(%s,%s,%s,%s)"""
                   ,(Branch_Switchers[ROLL]["ROLL"],Branch_Switchers[ROLL]["NAME"],Branch_Switchers[ROLL]["FROM_BRANCH"],Branch_Switchers[ROLL]["TO_BRANCH"]))


print "==================================================================================DETAILED DATABASE==================================================================================================="

print "\n"*2
print Detailed
print "\n"*2

print "========================================================================DATABASE WITH CARRY OVER DETAILS============================================================================="

print Detailed.get_string(fields=["ROLL", "NAME","PENDING1","STATUS1","PENDING1_CO","STATUS1_CO","PENDING2","STATUS2","PENDING2_CO","STATUS2_CO","PENDING3","STATUS3"])



print "==============================================================BRANCH CHANGERS==================================================================="
print "\n"*2
print bswitch

sql = """CREATE TABLE PRECISE AS
         SELECT ROLL,NAME,FATHER_NAME,SEM1_CO AS 1stSEM,SEM2_CO AS 2ndSEM,SEM3 AS 3rdSEM,SEM4 AS 4thSEM,SEM5 AS 5thSEM,SEM6 AS 6thSEM,(SEM1_CO+SEM2_CO+SEM3+SEM4+SEM5+SEM6) AS TOTAL
         FROM DETAILED"""

cursor.execute(sql)
                           #TO BE UPDATED AS PER CARRY OVERS RESULT ANNOUNCEMENT

ufm_table.add_row(["ODD SEMESTER 2015-16",UFM["ODD SEMESTER 2015-16"]])
cursor.execute("""INSERT INTO UFM(SEM,ROLLS)
                   VALUES(%s,%s)"""
                   ,("ODD SEMESTER 2015-16",UFM["ODD SEMESTER 2015-16"]))


print "\n===========================UNFAIR-MEANS CASES==========================\n"

print ufm_table

db.commit()
