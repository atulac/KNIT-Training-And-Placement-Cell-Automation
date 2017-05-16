import MySQLdb
import xlwt
import Range

def execute(table,year,branch,destination):                  #Takes in the input year, branch and destination path

    start=Range.RollRange1[(year,branch)][0]
    end=Range.RollRange1[(year,branch)][-1]                  #Extracts Range of Roll Numbers of specific branch and year
    Lateralstart=Range.RollRange2[(year,branch)][0]
    Lateralend=Range.RollRange2[(year,branch)][-1]           #Extracts Range of Roll Numbers of specific branch and year for LATERAL ENTRY

    workbook = xlwt.Workbook()
    sheet = workbook.add_sheet("TPCSheet")                   #Adds sheet to workbook to be created
    year=year.replace(" ","_")
    db1 = MySQLdb.connect(host="localhost",user="root",passwd="",db="TEMPDB")
    db2 = MySQLdb.connect(host="localhost",user="root",passwd="",db=year)


    """
    =========================================================================================================
    THE FOLLOWING CODE SNIPPET EXTRACTS DATA FROM MAIN DATABASE WITH THE HELP OF ROLL RANGE PROVIDED.
    THIS CREATES A TEMPORARY TABLE IN MYSQL DATABASE AND EXPORTS IT TO A SPECIFIED XLS FILE AT SPECIFIED PATH.
    =========================================================================================================
    """


    cur = db1.cursor()
    cur.execute("DROP TABLE IF EXISTS TEMP_TABLE")

    if table=='branch_changers' or table=='ufm':
        sql="CREATE TABLE TEMP_TABLE AS SELECT * FROM "+year+"."+table
    else:
        sql="CREATE TABLE TEMP_TABLE AS SELECT * FROM "+year+"."+table+" WHERE (ROLL BETWEEN "+str(start)+" AND "+str(end)+")\
        OR (ROLL BETWEEN "+str(Lateralstart)+" AND "+str(Lateralend)+")"

    cur.execute(sql)
    cur.execute("SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME='TEMP_TABLE' ORDER BY ORDINAL_POSITION")
    colNum=0

    style = xlwt.easyxf('font: bold 1')                     #SETS BOLD STYLE FOR FIRST ROW(COLUMN NAMES DATA)
    for each in cur.fetchall():
        sheet.write(0, colNum, each[0],style)               #each is a tuple values can be accessed by indexing
        colNum+=1

    if table=='ufm':
        cur.execute("SELECT * FROM TEMP_TABLE")             #to keep in ascending order of roll numbers
    else:
        cur.execute("SELECT * FROM TEMP_TABLE ORDER BY ROLL")
    rowNum=colNum=0

    """
      NOTE: You Can Call Cur.fetchall() only once
    """

    for rowNum,row in enumerate(cur.fetchall()) :
        for colNum,col in enumerate(row):
            sheet.write(rowNum+1, colNum, col)               #writes down other column data
            colNum += 1
        rowNum +=1

    workbook.save("TPCworkbook.xls")


    """
    ==========================================================================
    THE CODE SNIPPET BELOW MAKES OPERATION OVER PATH OF THE CURRENT DIRECTORY
    AND DESIRED MOVEMENT TO SPECIFIED DIRECTORY.

    backslash_map ENSURES THAT CERTAIN CHARACTERS MENTIONED AS KEY
    DO NOT GET REPLACED BY 0X CHARACTERS.
    ==========================================================================
    """

    backslash_map = { '\a': r'\a', '\b': r'\b', '\f': r'\f',
                  '\n': r'\n', '\r': r'\r', '\t': r'\t', '\v': r'\v' }

    import shutil,os

    #print "destination+="+destination
    source=os.getcwd()+"\TPCworkbook.xls"
    source=source.replace('\\','\\\\')

    for key,value in backslash_map.items():
        destination=destination.replace(key,value)
    destination=destination.replace('\\','\\\\')

    shutil.move(source,destination)


#execute('ufm','Third Year','CSE',"C:\Users\ayush894\Desktop\aaakh.xls")

