import random
from math import sqrt

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

    def create_slide(self, desc, i):
        slide_text = ""
        [x, y, scale, rotate] = self.get_random_vars(i)
        
        opening_div = "<div class='step' data-x='%d' data-y='%d' data-scale='%d' data-rotate='%d'>" % (x, y, scale, rotate)
        slide_text += opening_div
        slide_text += desc.get("text")
        
        imgs = desc.get("img_list")
        for img in imgs:
            slide_text += ("<img width='100%' src='" + img + "'/>")
        
        slide_text += "</div>"
        return slide_text
        
    def save_file(self, text, filename):
        with open(filename, "w") as text_file:
            text_file.write(text)
        
    def create_presentation(self, descs):
        with open("page_template.html") as f:
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

if __name__ == "__main__":
    descs = [
        {"text": "my first slide", "img_list": ["a.jpg"]},
        {"text": "my second slide", "img_list": ["b.jpg"]},
        {"text": "my third slide", "img_list": ["c.jpg"]},
        {"text": "my fourth slide", "img_list": ["d.jpg"]}]
    
    ic = ImpressCreator()
    ic.create_presentation(descs)
    