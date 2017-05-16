from bs4 import BeautifulSoup
from prettytable import PrettyTable

t=PrettyTable(["ROLL","NAME","FATHER_NAME","SEM1","SEM2","PENDING1","STATUS1","SEM1_CO","SEM2_CO","PENDING1_CO","STATUS1_CO","SEM3","SEM4",
               "PENDING2","STATUS2","SEM3_CO","SEM4_CO","PENDING2_CO","STATUS2_CO","SEM5"])
import urllib
import Range
import URL

def execute(Details,url,rolls,UFM):

    for ROLL in Range.RollRange[rolls]:
        site=URL.link[url]+str(ROLL)
        data=urllib.urlopen(site)
        soup = BeautifulSoup(data, 'html.parser')
        text=soup.get_text().splitlines()

        Details[ROLL]["ROLL"]=ROLL

        for line_index,line in enumerate(text):
            if 'UFM' in line.strip():
                Details[ROLL]["SEM5"]='UFM'
                UFM["ODD SEMESTER 2015-16"]+=" "+str(ROLL)+" "
            if line.strip()=='TOTAL MARKS':
                temp=text[line_index+1]
                try:
                     Details[ROLL]["SEM5"]=int(temp[:temp.index('/')])
                except:
                    print "ERROR ODD15_16"

        #t.add_row([Details[ROLL]["ROLL"],Details[ROLL]['NAME'],Details[ROLL]["FATHER's NAME"],Details[ROLL]["SEM1"],Details[ROLL]["SEM2"],Details[ROLL]["PENDING1"],
        #          Details[ROLL]["STATUS1"],Details[ROLL]["SEM1_CO"],Details[ROLL]["SEM2_CO"],Details[ROLL]["PENDING1_CO"],Details[ROLL]["STATUS1_CO"],Details[ROLL]["SEM3"],
        #          Details[ROLL]["SEM4"],Details[ROLL]["PENDING2"],Details[ROLL]["STATUS2"],Details[ROLL]["SEM3_CO"],Details[ROLL]["SEM4_CO"],Details[ROLL]["PENDING2_CO"],
        #          Details[ROLL]["STATUS2_CO"],Details[ROLL]["SEM5"]])

    #print t

    print "ODD15_16 DONE"





