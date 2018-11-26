import urllib
import urllib.request
from bs4 import BeautifulSoup


companies=["aapl","tsla","intu","amzn","fb","nvda","googl","msft","nflx","crm","orcl","dvmt"]



for i in companies:


    theurl = "https://www.nasdaq.com/symbol/" + i
    thepage =urllib.request.urlopen(theurl)
    soup = BeautifulSoup(thepage,"html.parser")
    print( i +"  is now trading for:",soup.find('div',{"class":"qwidget-dollar"}).text)













