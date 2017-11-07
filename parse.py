# bot
import bs4 
from bs4 import BeautifulSoup as soup
from urllib2 import urlopen

def news():
	# my_url = "https://news.google.com.hk/news/rss"

    my_url = "http://fortune.com/fortune500/list/"
	#To open the given URL
    Client = urlopen(my_url)
	
    xml_page=Client.read()
    Client.close()

    soup_page=soup(xml_page,"xml")
    news_list=soup_page.findAll("item")

    for news in news_list:
        print(news.title.text)
        print(news.link.text)
        print(news.pubDate.text)
        print("-"*n)

    n=input()
	
news()	