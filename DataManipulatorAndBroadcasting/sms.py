#!/usr/bin/python
import os
import urllib2
import cookielib
from getpass import getpass
import sys

#username = "8858218339"
#passwd = "M6734G"
#message = "gfchghjbkljfcgvhjbk"
#path='C:\Users\Ayush894\Desktop\New Text Document.txt'

def execute(path,username,passwd,message):

    statuspath=os.getcwd()+"\status.txt"
    print statuspath
    backslash_map = { '\a': r'\a', '\b': r'\b', '\f': r'\f',
                  '\n': r'\n', '\r': r'\r', '\t': r'\t', '\v': r'\v' }

    for key,value in backslash_map.items():
        statuspath=statuspath.replace(key,value)
        path=path.replace(key,value)

    status_file=open(statuspath,'w')
    status_file.write("SMS to the following numbers has been successfully sent.\n\n")
    numbers=[]
    message = "+".join(message.split(' '))

    #Logging into the SMS Site
    url = 'http://site24.way2sms.com/Login1.action?'
    data = 'username='+username+'&password='+passwd+'&Submit=Sign+in'

    #For Cookies:
    cj = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))

    # Adding Header detail:
    opener.addheaders = [('User-Agent','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120 Safari/537.36')]

    try:
        usock = opener.open(url, data)
    except IOError:
        print "Error while logging in."
        sys.exit(1)

    f=open(path,'r')
    for each in f.readlines():
        numbers.append(each.strip())

    for number in numbers:

        jession_id = str(cj).split('~')[1].split(' ')[0]
        send_sms_url = 'http://site24.way2sms.com/smstoss.action?'
        send_sms_data = 'ssaction=ss&Token='+jession_id+'&mobile='+number+'&message='+message+'&msgLen=136'
        opener.addheaders = [('Referer', 'http://site25.way2sms.com/sendSMS?Token='+jession_id)]

        try:
            sms_sent_page = opener.open(send_sms_url,send_sms_data)
        except IOError:
            print "Error while sending message"


        print "SMS has been sent."
        status_file.write(number+"\n")
    f.close()
    status_file.close()
    return statuspath


#path=execute(path,username,passwd,message)
#print path
#sys.exit(0)