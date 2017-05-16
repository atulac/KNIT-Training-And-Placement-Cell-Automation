from bs4 import BeautifulSoup
from collections import defaultdict
import urllib,Range,URL
from prettytable import PrettyTable

def execute(Details,url,rolls):

    t=PrettyTable(["ROLL","NAME","FATHER_NAME","SEM1","SEM2","PENDING1","STATUS1"])
    for ROLL in Range.RollRange[rolls]:
        site=URL.link[url]+str(ROLL)
        data=urllib.urlopen(site)
        soup = BeautifulSoup(data, 'html.parser')
        text=soup.get_text().splitlines()
        Details[ROLL]["ROLL"]=ROLL
        for line_index,line in enumerate(text):
            if line.strip()=='Name:':
                Details[ROLL]["NAME"]=text[line_index+1]
            elif line.strip()=='Carry Over Paper(Current Year)'or line.strip()=='PWG Paper(Current Year)':
                Details[ROLL]["PENDING1"]=text[line_index+1]
                if Details[ROLL]["PENDING1"].strip()==',':
                    Details[ROLL]["PENDING1"]='NONE'
            elif line.strip()=='First Year':
                temp=text[line_index+1]
                try:
                    Details[ROLL]["SEM2"]=int(temp[:temp.index('/')])-Details[ROLL]["SEM1"]
                except ValueError:
                    print "ERROR"
                    Details[ROLL]["SEM2"]=-1

                Details[ROLL]["STATUS1"]=text[line_index+2]

        #t.add_row([Details[ROLL]["ROLL"],Details[ROLL]['NAME'],Details[ROLL]["FATHER's NAME"],Details[ROLL]["SEM1"],Details[ROLL]["SEM2"],Details[ROLL]["PENDING1"],Details[ROLL]["STATUS1"]])

    #print t
    print "EVEN 13_14 DONE"






