from bs4 import BeautifulSoup
from collections import defaultdict
from prettytable import PrettyTable
import urllib,URL,Range

def execute(Details,url,rolls):

    t=PrettyTable(["ROLL","NAME","FATHER_NAME","SEM1","SEM2","PENDING1","STATUS1","SEM1_CO","SEM2_CO","PENDING1_CO","STATUS1_CO"])
    for ROLL in Range.RollRange[rolls]:
        site=URL.link[url]+str(ROLL)
        data=urllib.urlopen(site)
        soup = BeautifulSoup(data, 'html.parser')
        text=soup.get_text().splitlines()
        invalid='Roll Number not found in database'
        no_back=0
        for line_index,line in enumerate(text):
            if invalid in line:
                no_back=1
                break
            elif line.strip()=='Carry Over Paper(Current Year)'or line.strip()=='PWG Paper(Current Year)':
                Details[ROLL]["PENDING1_CO"]=text[line_index+1]
                if Details[ROLL]["PENDING1_CO"].strip()==',':
                    Details[ROLL]["PENDING1_CO"]='NONE'
            elif line.strip()=='First Year':
                temp=text[line_index+1]
                try:
                    Details[ROLL]["SEM2_CO"]=int(temp[:temp.index('/')])-Details[ROLL]["SEM1_CO"]
                except:
                    print "ERROR EVEN13_14CO"

                Details[ROLL]["STATUS1_CO"]=text[line_index+2]

        if Details[ROLL]["PENDING1"]=='NONE':
            Details[ROLL]["PENDING1_CO"]='NONE'
        if no_back==1:
            try:
                Details[ROLL]["SEM2_CO"]=Details[ROLL]["SEM2"]
            except:
                Details[ROLL]["SEM2_CO"]=-1

        if Details[ROLL]["PENDING1_CO"]=='NONE':
                    Details[ROLL]["STATUS1_CO"]="PASS"

        #t.add_row([Details[ROLL]["ROLL"],Details[ROLL]['NAME'],Details[ROLL]["FATHER's NAME"],Details[ROLL]["SEM1"],Details[ROLL]["SEM2"],
                      #Details[ROLL]["PENDING1"],Details[ROLL]["STATUS1"],Details[ROLL]["SEM1_CO"],Details[ROLL]["SEM2_CO"],Details[ROLL]["PENDING1_CO"],Details[ROLL]["STATUS1_CO"]])


    #print t
    print "EVEN13_14CO Done"






