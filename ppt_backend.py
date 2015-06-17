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

#*************************************************************************
# GREAT LINK:
# https://python-pptx.readthedocs.org/en/latest/user/quickstart.html
#*************************************************************************

from pptx import Presentation
from pptx.util import Inches, Pt



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


def add_contact_slide(prs, contact_dict):
    '''
    Optional: if we want to have contact slide
    Yoav suggest to pass it as a regular text if needed
    '''
    bullet_slide_layout = prs.slide_layouts[1]
    slide = prs.slides.add_slide(bullet_slide_layout)
    shapes = slide.shapes

    title_shape = shapes.title
    body_shape = shapes.placeholders[1]

    title_shape.text = 'Contact Details'

    tf = body_shape.text_frame
    tf.text = contact_dict["name"]
    if contact_dict.has_key("email"):
        p = tf.add_paragraph()
        p.text = contact_dict["email"]
    if contact_dict.has_key("phone"):
        p = tf.add_paragraph()
        p.text = contact_dict["phone"]

def add_text_slide(prs, slide_dict):
    blank_slide_layout = prs.slide_layouts[6]
    slide = prs.slides.add_slide(blank_slide_layout)
    #position of the text-box
    left = top = Inches(1)
    width = height = Inches(5)
    txBox = slide.shapes.add_textbox(left, top, width, height)
    tf = txBox.text_frame
    tf.text = slide_dict["text"]


def make_presentation():
    title_dict = {"title":"Go Go Slide-O-Matic",
                    "author":"Slide-O-Matic Team",
                    }#"image":"title_img.jpg"}

    contact_dict = {"name": "The marvelous Team\nTest",
                    "phone": "10-9",
                    "email": "marvelous@marvel.com"}
    slide1 = {"text": "* yair fodor\n* is one of the best\n* fuzball legs up player ever\n"}
    prs = Presentation()

    add_title_slide(prs, title_dict)
    add_text_slide(prs, slide1)
    #add_contact_slide(prs, contact_dict)
    prs.save('test.pptx')

if __name__ == '__main__':
    make_presentation({"first": {'title': 'Some Title', 'author': 'Yoav Glazner',
                                 }
                       
                       })
