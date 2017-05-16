from bs4 import BeautifulSoup
from prettytable import PrettyTable

import urllib,Range,URL

t=PrettyTable(["ROLL","NAME","FATHER_NAME","SEM1","SEM2","PENDING1","STATUS1","SEM1_CO","SEM2_CO","PENDING1_CO","STATUS1_CO","SEM3","SEM4",
               "PENDING2","STATUS2","SEM3_CO","SEM4_CO","PENDING2_CO","STATUS2_CO","SEM5","SEM6"])
def execute(Details,url,rolls):

    for ROLL in Range.RollRange[rolls]:
        """site=URL.link[url]+str(ROLL)
        data=urllib.urlopen(site)
        soup = BeautifulSoup(data, 'html.parser')
        text=soup.get_text().splitlines()

        Details[ROLL]["ROLL"]=ROLL

        for line_index,line in enumerate(text):
            if line.strip()=='Name:':
                Details[ROLL]["NAME"]=text[line_index+1]
            elif line.strip()=='Carry Over Paper(Current Year)'or line.strip()=='PWG Paper(Current Year)':
                Details[ROLL]["PENDING2"]=text[line_index+1]
                if Details[ROLL]["PENDING2"].strip()==',':
                    Details[ROLL]["PENDING2"]='NONE'
            elif line.strip()=='Second Year':
                temp=text[line_index+1]
                try:
                    Details[ROLL]["SEM4"]=int(temp[:temp.index('/')])-Details[ROLL]["SEM3"]
                except ValueError:
                    print "ERROR EVEN15_16"

                Details[ROLL]["STATUS2"]=text[line_index+2]"""

        #t.add_row([Details[ROLL]["ROLL"],Details[ROLL]['NAME'],Details[ROLL]["FATHER's NAME"],Details[ROLL]["SEM1"],Details[ROLL]["SEM2"],Details[ROLL]["PENDING1"],
        #          Details[ROLL]["STATUS1"],Details[ROLL]["SEM1_CO"],Details[ROLL]["SEM2_CO"],Details[ROLL]["PENDING1_CO"],Details[ROLL]["STATUS1_CO"],Details[ROLL]["SEM3"],
        #          Details[ROLL]["SEM4"],Details[ROLL]["PENDING2"],Details[ROLL]["STATUS2"],Details[ROLL]["SEM3_CO"],Details[ROLL]["SEM4_CO"],Details[ROLL]["PENDING2_CO"],
        #          Details[ROLL]["STATUS2_CO"],Details[ROLL]["SEM5"],Details[ROLL]["SEM6"]])

    #print t
    print "EVEN 15_16 DONE"






