from pandas import DataFrame
from dateutil.relativedelta import relativedelta
from datetime import timedelta
import numpy as np
import pandas as pd
from datetime import datetime
cols=[]
df1 = None

def execute(path):
    global df1
    backslash_map = { '\a': r'\a', '\b': r'\b', '\f': r'\f',
                  '\n': r'\n', '\r': r'\r', '\t': r'\t', '\v': r'\v' }

    for key,value in backslash_map.items():
        path=path.replace(key,value)

    global df
    df=pd.read_excel(path)
    global cols
    cols=list(df.columns.values)             #lists out the column names of the sheet
    df1=df
    return cols

def another():
    global df,df1
    df = df1

def convertToPercent():
    global df
    try:
        df['DOB'] = df['DOB'].apply(lambda x:x.date().strftime('%m-%d-%Y'))
    except:
        pass

    global cols
    if '1stSEM' in cols:
        df['1stSEM']=df['1stSEM'].div(10)
    if '2ndSEM' in cols:
        df['2ndSEM']=df['2ndSEM'].div(10)
    if '3rdSEM' in cols:
        df['3rdSEM']=df['3rdSEM'].div(10)
    if '4thSEM' in cols:
        df['4thSEM']=df['4thSEM'].div(10)
    if '5thSEM' in cols:
        df['5thSEM']=df['5thSEM'].div(10)
    if '6thSEM' in cols:
        df['6thSEM']=df['6thSEM'].div(10)
    if 'TOTAL' in cols:
        df['TOTAL']=df['TOTAL'].div(50)             #to be changed to 60 with 6th sem results

def totalRange(l,r):
    global df
    df=df[(df['TOTAL']>=l) & (df['TOTAL']<=r)]

def tenth(l,r):
    global df
    df=df[(df['10th']>=l) & (df['10th']<=r)]

def intermediate(l,r):
    global df
    df=df[(df['12th']>=l) & (df['12th']<=r)]

def dobRange(age,ref_date):
    global df

    d1 = datetime.strptime(ref_date, "%d-%m-%Y")
    d2=d1-relativedelta(years=age)
    df['temp']=d2
    df['DOB'] = pd.to_datetime(df['DOB'])
    df=df[df['DOB']>df['temp']]                        #the closer the date is to the current date, the bigger it is
    df['DOB'] = df['DOB'].apply(lambda x:x.date().strftime('%m-%d-%Y'))

    df.drop('temp', axis=1,inplace=True)

def yearGap(limit):
    pass#to be done

def toppers(n):
    global df
    df=df.sort_values(by='TOTAL',ascending=False)
    df=df[:n]                                       #TOTAL EVERYWHERE TO BE REPLACED BY AGGREGATE

def save(path):
    backslash_map = { '\a': r'\a', '\b': r'\b', '\f': r'\f',
                  '\n': r'\n', '\r': r'\r', '\t': r'\t', '\v': r'\v' }

    for key,value in backslash_map.items():
        path=path.replace(key,value)
    df.to_excel(path,index=False)






"""
execute('C:\Users\atulac\Desktop\vvvv.xls')
convertToPercent()
totalRange(70,90)
print df
toppers(10)
print df
dobRange(19,'18-03-2016')
print df
save('C:\Users\atulac\Desktop\aaa.xls')
"""






