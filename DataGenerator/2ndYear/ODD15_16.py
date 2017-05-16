from bs4 import BeautifulSoup
from prettytable import PrettyTable
import urllib
import Range
import URL

t=PrettyTable(["ROLL","NAME","FATHER_NAME","SEM1","SEM2","PENDING1","STATUS1","SEM1_CO","SEM2_CO","PENDING1_CO","STATUS1_CO","SEM3"])
bswitch=PrettyTable(["ROLL","NAME","FROM BRANCH","TO BRANCH"])
def execute(Details,url,rolls,Branch_Switchers,UFM):

    for ROLL in Range.RollRange[rolls]:
        site=URL.link[url]+str(ROLL)
        data=urllib.urlopen(site)
        soup = BeautifulSoup(data, 'html.parser')
        text=soup.get_text().splitlines()

        Details[ROLL]["ROLL"]=ROLL

        for line_index,line in enumerate(text):
            if 'UFM' in line.strip():
                Details[ROLL]["SEM3"]='UFM'
                UFM["ODD SEMESTER 2015-16"]+=" "+str(ROLL)+" "
            if line.strip()=='Name:':
                Details[ROLL]["NAME"]=text[line_index+1]
            elif line.strip()=="Father's Name:":
                Details[ROLL]["FATHER's NAME"]=text[line_index+1]
            elif line.strip()=="Course/Branch:":
                Details[ROLL]["BRANCH3"]=text[line_index+1]
                if Details[ROLL]["BRANCH3"]!=Details[ROLL]["BRANCH1"] and Details[ROLL]["BRANCH1"]!='-':
                    Branch_Switchers[ROLL]["ROLL"]=Details[ROLL]["ROLL"]
                    Branch_Switchers[ROLL]["NAME"]=Details[ROLL]["NAME"]
                    Branch_Switchers[ROLL]["FROM_BRANCH"]=Details[ROLL]["BRANCH1"]
                    Branch_Switchers[ROLL]["TO_BRANCH"]=Details[ROLL]["BRANCH3"]
                    bswitch.add_row([Branch_Switchers[ROLL]["ROLL"],Branch_Switchers[ROLL]["NAME"],Branch_Switchers[ROLL]["FROM_BRANCH"],Branch_Switchers[ROLL]["TO_BRANCH"]])
            elif line.strip()=='TOTAL MARKS':
                temp=text[line_index+1]
                try:
                    Details[ROLL]["SEM3"]=int(temp[:temp.index('/')])
                except:
                    print "ERROR ODD15_16"
       # t.add_row([Details[ROLL]["ROLL"],Details[ROLL]['NAME'],Details[ROLL]["FATHER's NAME"],Details[ROLL]["SEM1"],Details[ROLL]["SEM2"],Details[ROLL]["PENDING1"],
       #           Details[ROLL]["STATUS1"],Details[ROLL]["SEM1_CO"],Details[ROLL]["SEM2_CO"],Details[ROLL]["PENDING1_CO"],Details[ROLL]["STATUS1_CO"],Details[ROLL]["SEM3"]])
    #print t

    #print bswitch
    print "ODD15_16 DONE"







