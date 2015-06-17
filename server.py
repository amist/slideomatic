'''
Created on Jun 17, 2015

@author: yglazner
'''
from bottle import Bottle, run, static_file, post, request
import os
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
 
    data = request.json
    log.info ("data : %s", data) 
    if not data:
        return json.dumps({'Status':"Failed!"})
    else:
        core.generate(data.title, data.author, data.paragraphs, data.backend)
    return json.dumps({'Status':"Success!"})


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
