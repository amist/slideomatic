'''
Created on Jun 17, 2015

@author: yglazner
'''
from bottle import Bottle, run, static_file, post
import os
import core
app = Bottle()

@app.route('/')
def index():
    return static_file('index.html', 'web_client/src')

@app.route('/<path:path>')
def callback(path):
    for p in ( 'web_client/src', 'web_client',):
        if os.path.isfile(os.path.join(p, path)):
            return static_file( path, p)
    return static_file( path, p)

def main():
    app.run(host='0.0.0.0', port=8080, reloader=True, debug=1)
	
@post('/slides_data')
def create_slides():
    print "POST Header : \n %s" % dict(request.headers)
    data = request.json
    print "data : %s" % data 
    if data == None:
        return json.dumps({'Status':"Failed!"})
    else:
	core.generate(data.title, data.author, data.paragraphs, data.backend)
    return json.dumps({'Status':"Success!"})


    

    

if __name__ == '__main__':
    main()
