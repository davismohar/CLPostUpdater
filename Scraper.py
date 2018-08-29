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
    year = str(link.p)[timeIndex: timeIndex + 4]
    month = str(link.p)[timeIndex + 5: timeIndex + 7]
    day = str(link.p)[timeIndex + 8: timeIndex + 10]
    hour = str(link.p)[timeIndex + 11: timeIndex + 13]
    minute = str(link.p)[timeIndex + 14: timeIndex + 16]
    #finds the title of the post
    titleStartIndex = str(link.p).find(".html") + 7
    titleEndIndex = str(link.p).find("</a>", titleStartIndex, len(str(link.p)))
    title = str(link.p)[titleStartIndex: titleEndIndex]

    datetime.datetime(year, month, day)
    print(year + " " + month + " " + day + " " + hour + " " + minute)

    print(title)

    
