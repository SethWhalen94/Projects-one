import re
import requests
from io import BytesIO
from PIL import Image
from bs4 import BeautifulSoup

def saveFile(url):
    if len(url):
        img_link = requests.get(parse)
        img = Image.open(BytesIO(img_link.content))
        name = input("File name to save as: /n")
        img.save('./images/' + str(name) + '.' + img.format)

search = input('What would you like to search for? \n')
params = {'q': search}

r = requests.get("http://www.bing/images/search", params=params)

soup = BeautifulSoup(r.text, 'html.parser')

links = soup.find_all("img")

for image in links:
    parse = image.get("src")
    url = re.findall(r'^http.*', parse)
    saveFile(url)

