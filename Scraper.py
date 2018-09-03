import urllib2
from bs4 import BeautifulSoup
import datetime

#put url here
url = "https://blacksburg.craigslist.org/d/motorcycles-scooters/search/mca"

page = urllib2.urlopen(url)

soup = BeautifulSoup(page, "html.parser")
date = datetime.datetime.now()
print date
#splits the homepage into the posts
for link in soup.body.section.find_all("li"):
    #finds the post time
    timeIndex = str(link.p).find("datetime") + 10
    if timeIndex > 30:
        year = int(str(link.p)[timeIndex: timeIndex + 4])
        month = int(str(link.p)[timeIndex + 5: timeIndex + 7])
        day = int(str(link.p)[timeIndex + 8: timeIndex + 10])
        hour = int(str(link.p)[timeIndex + 11: timeIndex + 13])
        minute = int(str(link.p)[timeIndex + 14: timeIndex + 16])
        #finds the title of the post
        titleStartIndex = str(link.p).find(".html") + 7
        titleEndIndex = str(link.p).find("</a>", titleStartIndex, len(str(link.p)))
        title = str(link.p)[titleStartIndex: titleEndIndex]
        time = datetime.datetime(year, month, day, hour, minute)
        timedifference = datetime.datetime.now() - time
        print(time)
        print(timedifference)
        print(title)
        
        if(timedifference <= datetime.datetime.now() - datetime.datetime(0,0,0,12)):
            print("NEW POST")
        print("")

    
