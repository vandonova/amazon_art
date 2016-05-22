import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import time
import random

def encodestring(var):
    if var is not None:
        return var.encode('utf-8')

def scrapePainting(url):
    r = requests.get(url)
    print r, url
    b = BeautifulSoup(r.text, 'html.parser')
    
    url_id = r.url.split('/')[-1]
    
    artist = b.find('a', {'id':'fine-ART-ProductLabelArtistNameLink'})
    if artist is not None:
        artist = b.find('a', {'id':'fine-ART-ProductLabelArtistNameLink'}).text
        
    title = b.find('span', {'id': 'fineArtTitle'})
    if title is not None:
        title = b.find('span', {'id': 'fineArtTitle'}).text
        
    image = re.findall('http://ecx.images-amazon.com/images/I/.*\.jpg', r.text)
    if image is not None:
        image = re.findall('http://ecx.images-amazon.com/images/I/.*\.jpg', r.text)
        
    price = b.find('span', {'id': 'priceblock_ourprice'})
    if price is not None:
        price = b.find('span', {'id': 'priceblock_ourprice'}).text.replace('$','').replace(',', '')
        if '.' in price:
            price = float(price.replace('.', ''))/100
        else:
            price = float(price)
            
    desc = b.find('div', {'id': 'productDescription_feature_div'})
    if desc is not None:
        desc = b.find('div', {'id': 'productDescription_feature_div'}).getText().replace('\n','')
        
    height = None
    width = None
    size = b.find('span', {'id': 'mnba_buybox_size'})
    if size is not None:
        size = [a.strip() for a in b.find('span', {'id': 'mnba_buybox_size'}).text.split('x')]
        if len(size) == 2:
            height = float(size[0].replace('in.','').replace('in','').strip())
            width = float(size[1].replace('in.','').replace('in','').strip())
            depth = 1.
        elif len(size) == 3:
            height = float(size[0].replace('in.','').replace('in','').strip())
            width = float(size[1].replace('in.','').replace('in','').strip())
            depth = float(size[2].replace('in.','').replace('in','').strip())
    
    size_variations = b.find('div', {'id': 'variation_size_name'})
    if size_variations is not None:
        size = [a.strip() for a in size_variations.find('span', {'class': "a-size-base"}).text.split('x')]
        
        if len(size) == 2:
            height = float(size[0].replace('in.','').replace('in','').strip())
            width = float(size[1].replace('in.','').replace('in','').strip())
            depth = 1.
        elif len(size) == 3:
            height = float(size[0].replace('in.','').replace('in','').strip())
            width = float(size[1].replace('in.','').replace('in','').strip())
            depth = float(size[2].replace('in.','').replace('in','').strip())
            
        price = size_variations.find('span', {'class': "a-size-mini"}).text.replace('$','').replace(',', '')
        if '.' in price:
            price = float(price.replace('.', ''))/100
        else:
            price = float(price)
    

    return {'url_id': encodestring(url_id), 'artist': encodestring(artist), 'title':encodestring(title), 'image': image, 'price': price, 
            'description':encodestring(desc), 'height': height, 'width': width, 'size':size}

paintings = []

for page in range(1,219):
    
    page_url = 'http://www.amazon.com/s/ref=lp_6685289011_pg_2?rh=n%3A4991425011%2Cn%3A%214991426011%2Cn%3A6685269011%2Cn%3A6685289011&page='+str(page)+'&ie=UTF8&qid=1462681717'
    r = requests.get(page_url)
    r.text

    b = BeautifulSoup(r.text, 'html.parser')

    url_1 = []
    for link in b.findAll('a', {'class':"a-link-normal a-text-normal"}):
        url_1.append(link.get('href'))
    
    url_list = url_1[::2]

    for url in url_list:
        try:
            paintings.append(scrapePainting(url))
        except Exception as error:
            print error
        time.sleep(random.randint(5,20))
    
    if page % 10 == 0:
        df = pd.DataFrame(paintings)
        df.to_csv("output"+str(page)+".csv", index=False)

df = pd.DataFrame(paintings)

df.to_csv("final_df.csv", index=False)