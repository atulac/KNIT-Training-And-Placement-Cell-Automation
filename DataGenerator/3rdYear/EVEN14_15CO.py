from bs4 import BeautifulSoup
import urllib,URL,Range

def execute(Details,url,rolls):

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
                Details[ROLL]["PENDING2_CO"]=text[line_index+1]
                if Details[ROLL]["PENDING2_CO"].strip()==',':
                    Details[ROLL]["PENDING2_CO"]='NONE'
            elif line.strip()=='First Year':
                temp=text[line_index+1]
                try:
                    Details[ROLL]["SEM4_CO"]=int(temp[:temp.index('/')])-Details[ROLL]["SEM1_CO"]
                except:
                    print "ERROR EVEN14_15CO"
                Details[ROLL]["STATUS2_CO"]=text[line_index+2]

        if no_back==1:
            try:
                Details[ROLL]["SEM4_CO"]=Details[ROLL]["SEM4"]
            except TypeError,ValueError:
                Details[ROLL]["SEM4_CO"]=-1
            Details[ROLL]["STATUS1_CO"]="PASS"

    print "EVEN14_15CO Done"






