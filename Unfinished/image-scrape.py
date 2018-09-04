import re
import os
import requests
import random
import json
import codecs
import urllib.request
from urllib import request
from io import BytesIO
from PIL import Image
from bs4 import BeautifulSoup as bs

user_agent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
url = "https://www.pexels.com/search/HD%20wallpapers/"
url2 = "https://www.google.ca/search?q=hd+wallpapers&tbm=isch&tbo=u&source=univ&sa=X&ved=2ahUKEwiJleW90_LcAhWkCjQIHSiXB9wQsAR6BAgGEAE&biw=1440&bih=727#imgrc=_"
url3 = "https://bingwallpaper.com/"
url4 = "https://onlyhdwallpapers.com/"

'''
#? different way to parse url
res_2 = requests.get(url3) # enters website
soup = bs(res_2.text, "lxml") # downloads HTML as text and saves it in soup_2 vaiable

#print (soup_2)
#? End of secondary parsing

'''
#? first way of searching html text
headers = {"User-Agent" : random.choice(user_agent)}
req = requests.get(url,headers = headers)
#import pdb; pdb.set_trace()
html = req.text
soup = bs(html,'lxml') # downloads all html text from website
file_dir = os.getcwd()


#TODO: forloop finds all 'img' tags and pulls 'src' from them
for link in soup.find_all('a', ):
    image = link.get('src') #! gets src, direct link to jpeg URL
    #image = "http:" + str(link)
    question_mark = str(image).find("?")
    image = str(image)[:question_mark] #! removes resizing of image
    

    #todo : checks for nonsense URLs
    if ".pn" not in str(image) and "Non" not in str(image) and "/images/logo.gi" not in str(image): 
        print (image)
        image_name = os.path.split(image)[1] # gets the name of the image
        if ".pn" not in image_name:

            #urllib.request.urlretrieve(url,image_name)
            print (image)
            #?
            #req1 = requests.get(image)
            #img_obj = req1.content
            #print (img_obj)
            #img = Image.open(BytesIO(img_obj))
            #img.save("%s/%s" %(file_dir,image_name))

            #r2 = requests.get(image)
            #print (r2.content)
            #with open(image_name, "wb") as f:
             #   f.write(r2.content)

#? End of first way


#import pdb; pdb.set_trace()























'''def saveFile(url):
    if len(url):
        img_link = requests.get(parse)
        img = Image.open(BytesIO(img_link.content))
        name = input("File name to save as: /n")
        img.save('' + str(name) + '.' + img.format)

search = input('What would you like to search for? \n')
params = {'q': search}

r = requests.get("http://www.bing/images/search", params=params)

soup = BeautifulSoup(r.text, 'html.parser')

links = soup.find_all("img")

for image in links:
    parse = image.get("src")
    url = re.findall(r'^http.*', parse)
    saveFile(url)

'''