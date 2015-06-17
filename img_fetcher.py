import urllib
from urllib.parse import urlencode, quote
from urllib.request import urlopen
import json
from contextlib import closing
from pprint import pprint
import os
import threading
import shutil
from concurrent.futures import ThreadPoolExecutor
import logging
import random

log = logging.getLogger("img_fetcher")

NUMBER = 0

l = threading.Lock()

def get_number():
    global NUMBER
    with l:
        NUMBER+=1
        return NUMBER

def download(url):
    obj = urlopen(url)
    with closing(obj):
        return obj.read()

def delete_image_folder():
    if not os.path.isdir('images'): return
    shutil.rmtree('images')

def create_image_folder():
    if os.path.isdir("images"):
        return
    os.mkdir('images')

def get_pics(words):
    pics = list(_get_pics(words))
    return pics

def _get_image(r):
    number = get_number()
    url = r['url']
    extension = url[-3:].lower()
    if extension not in ('gif', 'jpg', 'png'):
        return
    try:
        img = download(url)
        path = "images/image_%d.%s" % (number, extension)
        with open(path, 'wb') as f: 
            f.write(img)
        return path
    except urllib.error.URLError:
        log.exception("url %s failed"% url)
        

def _get_pics(words):
   
    
    create_image_folder()
    words = quote(words)
    url = "https://ajax.googleapis.com/ajax/services/search/images?v=1.0&q={}".format(words)
    
    j = json.loads(download(url).decode('utf8'))
    if j['responseStatus'] != 200:
        return Exception("Bad status code getting image url=%s - code=%s" % (
                                                    url, j['responseStatus']))
                        
    if j.get('responseData') and j['responseData'].get('results'):
        results = j['responseData']['results']
        with ThreadPoolExecutor(max_workers=5) as tpe:
            for img in tpe.map(_get_image, results):
                if img: 
                    yield img
        
    
    
    
if __name__ == '__main__':
    delete_image_folder()    
    print(get_pics("mpeg4 layer are awesome"))