'''
Created on Jun 17, 2015

@author: yglazner
'''
from bottle import Bottle, run, static_file, post, request, get
import os
import zipfile
import core
import json
import logging
app = Bottle()
log = logging.getLogger("popcorn")
@app.route('/')
def index():
    return static_file('index.html', 'web_client/src')


@app.post('/slides_data')
def create_slides():
    log.info("in create slide")
    log.info("json data %s", request.json)
 
    data = request.json
    log.info ("data : %s", data)
    if not data:
        return json.dumps({'Status':"Failed!"})
    else:
        data = json.loads(data)
        core.generate(data['title'], data['author'], data['paragraphs'], data['backend'])
        log.info("done")
        return json.dumps({'Status':"Success!"})


def zip_impress_presentation():
    zipf = zipfile.ZipFile('my_impress.zip', 'w')
    zipf.write('slides.html')
    zipf.write('impress\css\impress-demo.css')
    zipf.write('impress\js\impress.js')
    for file in os.listdir("images"):
       zipf.write(os.path.join('images', file))
    zipf.close()
    return "my_impress.zip"


@app.get('/my_presentation')
def get_presentation():
    download_file = zip_impress_presentation()
    return static_file(download_file, root='.', download="my_impress.zip")





@app.route('/<path:path>')
def callback(path):
    log.info("path=%s", path)
    for p in ( 'web_client/src', 'web_client',):
        if os.path.isfile(os.path.join(p, path)):
            return static_file( path, p)
    return static_file( path, p)

def main():
    logging.basicConfig(level=1)
    app.run(host='0.0.0.0', port=8080, reloader=True, debug=1)
	


    

    

if __name__ == '__main__':
    main()
