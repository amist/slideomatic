'''
Created on Jun 17, 2015

@author: yglazner
'''
#import ppt_backend
from img_fetcher import get_pics, delete_image_folder
import logging

log = logging.getLogger("core")

BACKENDS = {
            'pttx': lambda data: 0#ppt_backend.make_presentation
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
        imgs = get_pics(para.replace('\n', ' '))
        slides.append({
                       "text": para,
                       "images": imgs,
                       "qoute": None,
                       "buzz": None,
                       })
    log.debug("sending %s to %s" % (data, backend))
    backend(data)
    log.info("DONE :)")


        
    
    
    

    