from bs4 import BeautifulSoup
from collections import defaultdict
from prettytable import PrettyTable
import urllib,URL,Range

def execute(Details,url,rolls):

    t=PrettyTable(["ROLL","NAME","FATHER_NAME","SEM1","SEM2","PENDING1","STATUS1","SEM1_CO"])
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
            elif line.strip()=='First Year':
                temp=text[line_index+1]
                try:
                    Details[ROLL]["SEM1_CO"]=int(temp[:temp.index('/')])-Details[ROLL]["SEM2"]
                except:
                    print "ERROR ODD13_14CO"

        if no_back==1:
                Details[ROLL]["SEM1_CO"]=Details[ROLL]["SEM1"]

        #t.add_row([Details[ROLL]["ROLL"],Details[ROLL]['NAME'],Details[ROLL]["FATHER's NAME"],Details[ROLL]["SEM1"],Details[ROLL]["SEM2"],Details[ROLL]["PENDING1"],Details[ROLL]["STATUS1"],Details[ROLL]["SEM1_CO"]])

    #print t

    print "CO 13_14 Done"






