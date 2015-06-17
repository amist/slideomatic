#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      yfodor
#
# Created:     17/06/2015
# Copyright:   (c) yfodor 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------



from pptx import Presentation
from pptx.util import Inches
import urllib2

def download_title_img(img_url, img_name):
    '''

    '''
    imgRequest = urllib2.Request(img_url, headers={'User-Agent' :'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'})
    imgData = urllib2.urlopen(imgRequest).read()

    f = open(img_name,'wb')
    f.write(imgData)
    f.close()


def add_title_slide(prs, title_dict):
    '''
    The function get dictionary with the following keys and create title slide:
        title - the title of the presentation
        author - the name of the author - will present in the bottom of the slide
        img_title - path to the image. if picture is not needed this key is not valid
    '''
    title_slide_layout = prs.slide_layouts[0]
    slide = prs.slides.add_slide(title_slide_layout)
    title = slide.shapes.title
    subtitle = slide.placeholders[1]

    title.text = title_dict["title"]
    subtitle.text = title_dict["author"]
    if(title_dict.has_key("image")):
        top = Inches(1)
        left = Inches(3)
        height = Inches(3)

        pic = slide.shapes.add_picture(title_dict["image"], left, top, height=height)


def contact_slide(prs, contact_dict):
    pass

def make_presentation():
    title_dict = {"title":"Go Go Slide-O-Matic",
                    "author":"Slide-O-Matic Team",
                    }#"image":"title_img.jpg"}
    prs = Presentation()

    add_title_slide(prs, title_dict)

    prs.save('test.pptx')

make_presentation()
