import bs4
from bs4 import BeautifulSoup
import urllib.request
import urllib.parse

# link = "https://www.dynamsoft.com/blog/"
link = "https://www.dynamsoft.com/Products/WebTWAIN_Overview.aspx"
f = urllib.request.urlopen(link)
myfile = f.read()
f.close()
print(myfile)

# def news():
    # my_url = "http://rss.nytimes.com/services/xml/rss/nyt/Technology.xml"
    # Client = urllib.request.urlopen(my_url)
    # print(Client)

    # xml_page = Client.read()
    # Client.close()

    # soup_page = soup(xml_page, "xml")
    # news_list = soup_page.findParent("item")
    # soup_page.find

    # for news in news_list:
    #     print(news.title.text)
    #     print(news.link.text)
    #     print(news.pubDate.text)
    #     print("-"*n)

    # n = input()

# news()

# def musical():
#     params = urllib.parse.urlencode({'spam':1, 'eggs':2, 'bacon':0})
#     url = "http://www.musi-cal.com/cgi-bin/query?%s" % params
#     with urllib.request.urlopen(url) as f:
#         print(f.read().decode('utf-8'))

# musical()

# def html():
#     url = "http://www.nytimes.com/services/xml/rss/index.html"
#     with open(url) as fp:
#         soup = BeautifulSoup(fp)

#     soup = BeautifulSoup("<html>data</html>")

# html()