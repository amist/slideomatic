'''
Created on Jun 17, 2015

@author: yglazner
'''
#import ppt_backend
from img_fetcher import get_pics, delete_image_folder
import impress.creator
import logging
import wiki_sentence_generator

log = logging.getLogger("core")

BACKENDS = {
            'pttx': lambda data: 0,#ppt_backend.make_presentation
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
        buzz = wiki_sentence_generator.random_wiki_sentence(para)
        imgs = get_pics(para.replace('\n', ' '))
        slides.append({
                       "text": para,
                       "images": imgs,
                       "quote": None,
                       "buzz": buzz,
                       })
    log.debug("sending %s to %s" % (data, backend))
    backend(data)
    log.info("DONE :)")


        
    
    
    

    