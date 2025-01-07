import smtplib, ssl
import os



def send_email(message):
    host="smtp.gmail.com"
    port=465

    username="osrarts@gmail.com"
    #password=os.getenv("PASSWORD")
    password="qelv psie sizz dzjh"


    receiver="osrarts@gmail.com"
    context=ssl.create_default_context()

    #message="""\ This is python generated msg by suchitra"""

    with smtplib.SMTP_SSL(host,port,context=context) as server:
        server.login(username,password)
        server.sendmail(username,receiver,message)
