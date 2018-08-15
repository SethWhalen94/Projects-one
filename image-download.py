from bs4 import BeautifulSoup
from datetime import datetime as dt
import requests
import urllib.request
from urllib import request

pic_url = 'https://www.pexels.com/search/HD%20wallpaper/'
res = requests.get(pic_url)
#resp = request.urljoin(pic_url)

soup = BeautifulSoup(res.text, 'lxml')

product = soup.find('div',{'class': 'sfbgx'})


image_box = soup.find('a', {'class': 'js-photo-link'}) #where 'a' is the anchor element, and the class name is 'cursor_zoom'
image = image_box.find('img') # finds 'img' tag, start of image url

link = image['srcset'] # src = photo url


file_name = dt.now().strftime('%m-%d-%y') # creates month-day-year name

#urllib.request.urlretrieve(link, '/home/rudy/Pictures/%s' %file_name) # retrives img file from URL, saves it in picture folder with today's date

print(link)