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
            if sqrt((pu_x - x)**2 + (pu_y - y)**2) < (1000 * pu_s):
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

    def create_slide(self, desc, i):
        slide_text = ""
        [x, y, scale, rotate] = self.get_random_vars(i)
        
        opening_div = "<div class='step' data-x='%d' data-y='%d' data-scale='%d' data-rotate='%d'>" % (x, y, scale, rotate)
        slide_text += opening_div
        slide_text += self.process_text(desc.get("text"))
        
        imgs = desc.get("images")
        for img in imgs:
            slide_text += ("<img width='100%' src='" + img + "'/>")
        
        slide_text += "</div>"
        return slide_text
        
    def save_file(self, text, filename):
        with open(filename, "w") as text_file:
            text_file.write(text)
        
    def create_presentation(self, data):
        print("----")
        print(data)
        print("----")
        
        descs = data['slides']
        with open(p("page_template.html")) as f:
            page_template = f.readlines()
            page_template = "".join(page_template)
            
            slides_text = ""
            i = 0
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
        css_text += "\n"
        
        self.save_file(css_text, "style.css")
        
def generate(data):
    ic = ImpressCreator()
    ic.create_presentation(data)
    ic.create_css()
    
if __name__ == "__main__":
    descs = [
        {"text": "my first slide", "images": ["a.jpg"]},
        {"text": "my second slide", "images": ["b.jpg"]},
        {"text": "my third slide", "images": ["c.jpg"]},
        {"text": "my fourth slide", "images": ["d.jpg"]}]
        
    data = {'slides': descs}
    
    ic = ImpressCreator()
    ic.create_presentation(data)
    ic.create_css()
    