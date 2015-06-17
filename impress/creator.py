import random
from math import sqrt
import os

FOLDER = os.path.split(__file__)[0]
p = lambda s: os.path.join(FOLDER, s)

class ImpressCreator(object):

    def __init__(self):
        self.params_used = []
        
    def validate_random_vars(self, vars):
        [x, y, scale, rotate] = vars
        for pu in self.params_used:
            pu_x = pu.get("x")
            pu_y = pu.get("y")
            pu_s = pu.get("scale")
            if sqrt((pu_x - x)**2 + (pu_y - y)**2) < (1500 * pu_s) or sqrt((pu_x - x)**2 + (pu_y - y)**2) < (1500 * scale):
                return False
        return True
        
    def get_random_vars(self, i):
        heat = 1
        while True:
            x = 1000 * i + random.randint(-500*heat, 500*heat)
            y = 1000 * i + random.randint(-500*heat, 500*heat)
            scale = random.randint(1, 5)
            rotate = random.randint(0, 359)
            if not self.validate_random_vars([x, y, scale, rotate]):
                heat += 1
                continue
            self.params_used.append({"x": x, "y": y, "scale": scale, "rotate": rotate})
            return [x, y, scale, rotate]
            
    def process_text(self, text):
        words = text.split(" ")
        words = ["<span class='rand_rotate'>" + word + "</span>" if random.randint(0, 4) == 1 else word for word in words]
        #for word in words:
        #    if random.randint(0, 4) == 1:
        #        word = "<span class='rand_rotate'>" + word + "</span>"
        text = " ".join(words)
        return text
        
    def create_first_page(self, desc):
        slide_text = ""
        opening_div = "<div class='step' data-x='0' data-y='0' data-scale='1' data-rotate='0'>"
        slide_text += opening_div
        slide_text += "<div style='position: fixed; top: -200px; left: 0'>"
        slide_text += "<div class='bigText'>" + desc['title'] + "</div>"
        slide_text += "<div>" + desc['author'] + "</div>"
        slide_text += "</div>"
        slide_text += ("<img style='max-height: 400px; max-width: 700px; position: fixed; top: 0; left: 400px;' src='" + desc['image'] + "'/>")
        slide_text += "</div>"
        self.params_used.append({"x": 0, "y": 0, "scale": 1, "rotate": 0})
        return slide_text
        
    def create_img_elements(self, imgs, text_up):
        imgs_text = ""
        max_imgs_num = random.randint(2, 3)
        imgs_num = min(len(imgs), max_imgs_num)
        if imgs_num == 1:
            img_width = 70
        else:
            img_width = 100 / sqrt(imgs_num)
        i = 0
        left_before_right = random.randint(0, 1) == 0
        for img in imgs:
            t = 0
            l = 0
            if i >= imgs_num:
                break
            upper_bound = max(int(300 - 100 * img_width / 25), 1)
            if text_up:
                t = random.randint(0, 100)
            else:
                t = random.randint(-400, -200)
            if imgs_num == 1 or imgs_num == 3:
                if i == 0:
                    l = 10
                if i == 1 and left_before_right or i == 2 and not left_before_right:
                    l = -30 - random.randint(1, 10)
                if i == 2 and left_before_right or i == 1 and not left_before_right:
                    l = 67 + random.randint(1, 15)
            else: # imgs_num == 2:
                if i == 0 and left_before_right or i == 1 and not left_before_right:
                    l = -25 - random.randint(1, 10)
                if i == 1 and left_before_right or i == 0 and not left_before_right:
                    l = 45 + random.randint(1, 15)
            i += 1
            img_tag = ("<img style='max-height: 400px; max-width: %d%%; position: fixed; top: %d%%; left: %d%%;' src='" + img + "'/>") % (img_width, t, l)
            imgs_text += img_tag
            img_width /= 1.5
            if img_width < 20:
                break
        return imgs_text

    def create_slide(self, desc, i):
        slide_text = ""
        [x, y, scale, rotate] = self.get_random_vars(i)
        
        opening_div = "<div class='step' data-x='%d' data-y='%d' data-scale='%d' data-rotate='%d'>" % (x, y, scale, rotate)
        slide_text += opening_div
        
        imgs = desc.get("images")
        text_up = random.randint(0, 2) == 0
        #print("text up" if text_up else "text down")
        slide_text += self.create_img_elements(imgs, text_up)
        
        if text_up:
            slide_text += "<div class='textDiv' style='position: fixed; top: -200px; left: 0px;'>"
        else:
            slide_text += "<div class='textDiv' style='position: fixed; top: 200px; left: 0px;'>"
        slide_text += self.process_text(desc.get("text"))
        slide_text += "</div>"
        
        #for img in imgs:
        #    slide_text += ("<img width='100%' src='" + img + "'/>")
        
        slide_text += "</div>"
        return slide_text
        
    def save_file(self, text, filename):
        with open(filename, "w") as text_file:
            text_file.write(text)
        
    def create_presentation(self, data):
        #print("----")
        #print(data)
        #print("----")
        
        descs = data['slides']
        with open(p("page_template.html")) as f:
            page_template = f.readlines()
            page_template = "".join(page_template)
            
            slides_text = ""
            
            first_page = self.create_first_page(data['first'])
            slides_text += first_page
            slides_text += "\n"
            
            i = 1
            for desc in descs:
                cur_slide = self.create_slide(desc, i)
                slides_text += cur_slide
                slides_text += "\n"
                
                i += 1
            
            page = page_template % slides_text
            self.save_file(page, "slides.html")
            
            #print(page)
            #print(self.params_used)
            
    def create_css(self):
        rotate = 7 * (random.randint(-3, 4) + 0.5)
        transition = random.uniform(0, 2)
        css_text = ""
        css_text += ".present .rand_rotate {"
        css_text += "\n"
        css_text += ("-webkit-transform: rotate(%ddeg);" % rotate)
        css_text += "\n"
        css_text += ("-moz-transform:    rotate(%ddeg);" % rotate)
        css_text += "\n"
        css_text += ("-ms-transform:    rotate(%ddeg);" % rotate)
        css_text += "\n"
        css_text += ("-o-transform:    rotate(%ddeg);" % rotate)
        css_text += "\n"
        css_text += ("transform:         rotate(%ddeg);" % rotate)
        css_text += "\n"
        css_text += "display: inline-block;"
        css_text += "\n"
        css_text += ("-webkit-transition: %.2fs;" % transition)
        css_text += "\n"
        css_text += ("-moz-transition:    %.2fs;" % transition)
        css_text += "\n"
        css_text += ("-ms-transition:     %.2fs;" % transition)
        css_text += "\n"
        css_text += ("-o-transition:      %.2fs;" % transition)
        css_text += "\n"
        css_text += ("transition:         %.2fs;" % transition)
        css_text += "\n"
        css_text += "}"
        css_text += """\n
.textDiv b {
    display: block;
}

.bigText {
    font-size: 100px;
}

.mediumText {
    font-size: 65px;
}
"""
        
        
        self.save_file(css_text, "style.css")
        
def generate(data):
    ic = ImpressCreator()
    ic.create_presentation(data)
    ic.create_css()
    
if __name__ == "__main__":
    descs = [
        {"text": "my first slide", "images": ["a.jpg"]},
        {"text": "my second slide", "images": ["a.jpg", "b.jpg"]},
        {"text": "my third slide", "images": ["a.jpg", "b.jpg", "c.jpg"]},
        {"text": "my fourth slide", "images": ["d.jpg"]}]
    
    first = {'title': 'My Title', 'image': 'a.jpg', 'author': 'John Smith'}
        
    data = {
        'slides': descs,
        'first': first
        }
    
    ic = ImpressCreator()
    ic.create_presentation(data)
    ic.create_css()
    