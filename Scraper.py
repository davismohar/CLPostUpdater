import urllib2
from bs4 import BeautifulSoup
import datetime
import smtplib

#email server
server = "stmp.gmail.com"
#put url here
URL = ""
#how often this program is run (in minutes)
#this is how new posts are determined
UPDATE_RATE = 120
page = urllib2.urlopen(URL)
#enter email username and password
username = ""
password = ""
#email recipient
recipient = ""
#the subject line of the email
subject = ""
msg = """\
From: %s
To: %s
Subject: %s


"""%username, recipient, subject
def connect(server, username, password):
    #connects to the email server
    try:
        server = smtplib.SMTP(server, 587)
        server.starttls()
        server.ehlo()
        print("Connect success")
        server.login(username, password)
    except:
        print("Failed to connect to server")
        msg = "failed to authenticate, please make sure email settings are correct"
        server.sendmail(username, recipient, msg) 


def parse():
    soup = BeautifulSoup(page, "html.parser")
    #splits the homepage into the posts
    for link in soup.body.section.find_all("li"):
        #finds the post time
        timeIndex = str(link.p).find("datetime") + 10
        #This was a simple way to prevent other links from showing up
        if timeIndex > 30:
            year = int(str(link.p)[timeIndex: timeIndex + 4])
            month = int(str(link.p)[timeIndex + 5: timeIndex + 7])
            day = int(str(link.p)[timeIndex + 8: timeIndex + 10])
            hour = int(str(link.p)[timeIndex + 11: timeIndex + 13])
            minute = int(str(link.p)[timeIndex + 14: timeIndex + 16])
            time = datetime.datetime(year, month, day, hour, minute)
            timedifference = datetime.datetime.now() - time
            #if the post timestamp is within the update rate, then it is considered a new post and displayed
            if(timedifference.days == 0 and timedifference.seconds < UPDATE_RATE*60):
                #finds the title of the post
                titleStartIndex = str(link.p).find(".html") + 7
                titleEndIndex = str(link.p).find("</a>", titleStartIndex, len(str(link.p)))
                title = str(link.p)[titleStartIndex: titleEndIndex]
                #finds the price
                priceStartIndex = int(str(link.p).find("result-price") + 15)
                priceEndIndex = str(link.p).find("</span>", priceStartIndex, len(str(link.p)))
                #if there is no price, then default to 0
                if (priceStartIndex > 100):
                    price = str(link.p)[priceStartIndex: priceEndIndex]
                else:
                    price = 0
                #finds the link
                addressStartIndex = str(link.p).find("href") + 6
                addressEndIndex = titleStartIndex - 2
                address = str(link.p)[addressStartIndex: addressEndIndex]
                
                msg = msg + title + "\n" + "time: " + str(time) + "\nprice: " + price + "\n" + address + "\n\n\n\n"

                

def sendMail(server, msg):
    #if the message is empty, then dont send
    if (len(msg) > 10):     
        server.sendmail(username, recipient, msg)  
        print("email sent")
        server.quit()
    else:
        print("no new posts were found")
        server.quit()

if __name__ == "__main__":
    connect(server, username, password)
    parse()
    sendMail(server, msg)


       
    
