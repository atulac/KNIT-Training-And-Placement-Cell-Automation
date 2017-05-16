import smtplib
import os
import sys
import socket
from email.mime import multipart,text,base
from email import encoders

def execute(sender,password,recipients,subject,body,attachments):
    print sender,password,recipients,subject,body,attachments

    backslash_map = { '\a': r'\a', '\b': r'\b', '\f': r'\f',
                  '\n': r'\n', '\r': r'\r', '\t': r'\t', '\v': r'\v' }
    for key,value in backslash_map.items():
        recipients=recipients.replace(key,value)

    recipients=recipients.replace('\\','\\\\')

    f=open(recipients,'r')
    recipients=' '.join(f.readlines())

    msg = multipart.MIMEMultipart()
    msg['From'] = sender
    msg['To'] = recipients
    msg['Subject'] = subject

    msg.attach(text.MIMEText(body, 'plain'))


    for filename in attachments:
            f = filename

            for key,value in backslash_map.items():
                f=f.replace(key,value)
            f=f.replace('\\','\\\\')

            part = base.MIMEBase('application', "octet-stream")
            part.set_payload( open(f,"rb").read() )
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(f))
            msg.attach(part)


    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.set_debuglevel(False)

        server.starttls()
        server.login(sender,password)

    except socket.gaierror:
        print "Check your Internet Connection"
        return 2
    except smtplib.SMTPAuthenticationError:
        print "Invalid Username or Password"
        return 3
    except:
        print "Login Failed"
        return 4

    try:
        server.sendmail(msg['From'], recipients.split(), msg.as_string())
        print 'Email Sent Successfully'
        server.quit()
        return 1
    except:
        print "Email Not Sent"
        return 0

#execute(sender,password,recipients,subject,body,attachments)

