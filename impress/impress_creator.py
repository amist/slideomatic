class ImpressCreator(object):

    def create_slide(self, desc, i):
        slide_text = ""
        opening_div = "<div class='step slide' data-x='%d' data-y='%d'>" % (1000 * i, 1000 * i)
        slide_text += opening_div
        slide_text += desc.get("text")
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
            print(page)
            self.save_file(page, "slides.html")

if __name__ == "__main__":
    descs = [{"text": "my first slide"}, {"text": "my second slide"}]
    
    ic = ImpressCreator()
    ic.create_presentation(descs)
    