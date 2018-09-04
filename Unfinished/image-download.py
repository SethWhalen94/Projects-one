import requests
import random
import urllib.request
from urllib import request
from bs4 import BeautifulSoup as bs

url = "https://www.pexels.com/search/HD%20wallpaper/"




user_agent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"

headers = {"User-Agent" : random.choice(user_agent)}
req = requests.get(url,headers = headers)
#import pdb; pdb.set_trace()
html = req.text
soup = bs(html,'lxml') # downloads all html text from website


#r = requests.get(url)

#soup = bs(r.text, "html.parser")

#print (soup)
soup = soup.find("a", {"class" : "js-photo-link" })
soup = soup.find ("href")
print (soup)