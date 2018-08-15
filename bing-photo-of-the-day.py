from bs4 import BeautifulSoup
from datetime import datetime as dt
import requests
import urllib.request

res = requests.get('https://bingwallpaper.com/')

soup = BeautifulSoup(res.text, 'lxml')
image_box = soup.find('a', {'class': 'cursor_zoom'}) #where 'a' is the anchor element, and the class name is 'cursor_zoom'
image = image_box.find('img') # finds 'img' tag, start of image url

link = image['src'] # src = photo url


file_name = dt.now().strftime('%m-%d-%y') # creates month-day-year name


urllib.request.urlretrieve(link, '/home/rudy/Pictures/%s' %file_name) # retrives img file from URL, saves it in picture folder with today's date
