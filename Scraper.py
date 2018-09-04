import urllib2
from bs4 import BeautifulSoup
import datetime

#put url here
URL = "https://blacksburg.craigslist.org/d/motorcycles-scooters/search/mca"
#how often this program is run (in minutes)
#this is how new posts are determined
UPDATE_RATE = 3600
page = urllib2.urlopen(URL)

soup = BeautifulSoup(page, "html.parser")
date = datetime.datetime.now()
print date
#splits the homepage into the posts
for link in soup.body.section.find_all("li"):
    #finds the post time
    timeIndex = str(link.p).find("datetime") + 10
    #This if was a simple way to prevent other links from showing up
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
            print("NEW POST")
            #finds the title of the post
            titleStartIndex = str(link.p).find(".html") + 7
            titleEndIndex = str(link.p).find("</a>", titleStartIndex, len(str(link.p)))
            title = str(link.p)[titleStartIndex: titleEndIndex]
            priceStartIndex = int(str(link.p).find("result-price") + 15)
            priceEndIndex = str(link.p).find("</span>", priceStartIndex, len(str(link.p)))
            if (priceStartIndex > 100):
                price = str(link.p)[priceStartIndex: priceEndIndex]
            else:
                price = 0
            addressStartIndex = str(link.p).find("href") + 6
            addressEndIndex = titleStartIndex - 2
            address = str(link.p)[addressStartIndex: addressEndIndex]
            print(time)
            print(title)
            print(price)
            print(address)
            print("") 
        
          
       
    
