from bs4 import BeautifulSoup
from collections import defaultdict
from prettytable import PrettyTable

import urllib
import Range
import URL
table=[[]]

def execute(Details,url,rolls):


    t=PrettyTable(["ROLL","NAME","FATHER_NAME","SEM1"])
    for ROLL in Range.RollRange[rolls]:
        site=URL.link[url]+str(ROLL)
        data=urllib.urlopen(site)
        soup = BeautifulSoup(data, 'html.parser')
        text=soup.get_text().splitlines()

        Details[ROLL]["ROLL"]=ROLL
        for line_index,line in enumerate(text):
            if line.strip()=='Name:':
                Details[ROLL]["NAME"]=text[line_index+1]
            elif line.strip()=="Father's Name:":
                Details[ROLL]["FATHER's NAME"]=text[line_index+1]
            elif line.strip()=="Course/Branch:":
                Details[ROLL]["BRANCH1"]=text[line_index+1]
            elif line.strip()=='TOTAL MARKS':
                temp=text[line_index+1]
                Details[ROLL]["SEM1"]=int(temp[:temp.index('/')])

        #t.add_row([Details[ROLL]["ROLL"],Details[ROLL]["NAME"],Details[ROLL]["FATHER's NAME"],Details[ROLL]["SEM1"]])

    #print t
    print "\nODD13_14 DONE"





