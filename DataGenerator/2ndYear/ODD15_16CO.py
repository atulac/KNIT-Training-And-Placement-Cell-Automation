from bs4 import BeautifulSoup
import urllib
import Range
import URL

def execute(Details,url,rolls,Branch_Switchers):

    for ROLL in Range.RollRange[rolls]:
        site=URL.link[url]+str(ROLL)
        data=urllib.urlopen(site)
        soup = BeautifulSoup(data, 'html.parser')
        text=soup.get_text().splitlines()
        invalid='Roll Number not found in database'
        Details[ROLL]["ROLL"]=ROLL
        no_back=0

        for line_index,line in enumerate(text):
            if invalid in line:
                no_back=1
                break
            elif line.strip()=='Second Year':
                temp=text[line_index+1]
                try:
                    Details[ROLL]["SEM3_CO"]=int(temp[:temp.index('/')])-Details[ROLL]["SEM4"]
                except:
                    print "ERROR ODD14_15CO"

        if no_back==1:
                Details[ROLL]["SEM3_CO"]=Details[ROLL]["SEM3"]


    print "ODD14_15CO DONE"







