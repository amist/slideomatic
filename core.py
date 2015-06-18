'''
Created on Jun 17, 2015

@author: yglazner
'''
#import ppt_backend
from img_fetcher import get_pics, delete_image_folder
import impress.creator
import logging
import wiki_sentence_generator
from quotes_fetcher import fetch_quote
from ppt_backend import make_presentation
from wiki_sentence_generator import random_wiki_sentence

log = logging.getLogger("core")

BACKENDS = {
            'pttx': make_presentation,
            'impress': impress.creator.generate
            }

def generate(title, author, paragraghs, backend='pttx'):
    delete_image_folder()
    backend = BACKENDS[backend]
    slides = []
    imgs = get_pics(title.replace('\n', ' '))
    data = {
            'first': {
                      'title': title,
                      'author': author,
                      'image': imgs[0] if imgs else None,
                      
                      },
            'slides': slides
            
            }
    
    
    for para in paragraghs:
        
        if para.startswith('WIKI:'):
            para = random_wiki_sentence(para[5:])
        buzz = ""
        quote = ""#fetch_quote(para)
        imgs = get_pics(para.replace('\n', ' '))
        slides.append({
                       "text": para,
                       "images": imgs,
                       "quote": quote,
                       "buzz": buzz,
                       })
    log.debug("sending %s to %s" % (data, backend))
    backend(data)
    log.info("DONE :)")


        
    
    
    

    