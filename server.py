'''
Created on Jun 17, 2015

@author: yglazner
'''
from bottle import Bottle, run, static_file
import os

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
    

if __name__ == '__main__':
    main()