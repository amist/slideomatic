'''
Created on Jun 17, 2015

@author: yglazner
'''
import sys;sys.path.insert(0, '.')
import core
from core import BACKENDS
import logging
import time
import pack
import os
import webbrowser

        
def save(a):
    with open('lastrun', 'a') as f:
        f.write(a+"\n")
       
def inp(s):
    a = ''
    while not a.strip():
        a = input(s)
        save(a)
        
    return a.strip()

def main():
    print("Welcome!\n")
    with open('lastrun' ,'wb'): 
        pass
    title = inp("Title:\n")
    
    author = inp("Author:\n")
    paragraphs = []
    for i in range(1, 2000):
        para = inp("Insert text for slide %d(w=wikipedia, q=quit):"%i)
        if para.strip() in 'qQ':
            break
        elif para.strip() in 'wW':
            para = "WIKI:"+inp("Wiki subject:")
        else:
            line = '*'
            while 1:
                line = input("")
                save(line)
                if not line: break
                para += '\n' + line
    
        paragraphs.append(para)
    backend = ''
    #while backend not in BACKENDS:
    #    backend = inp("Backend [%s]:\n"% ", ".join(BACKENDS.keys()))
    backend = 'impress'
        
    core.generate(title, author, paragraphs, backend)
    time.sleep(0.2)
    title = title.replace(" ", "_") + "_%s" % int(time.time())
    pack.main(title)
    print("Yay we are done!")
    fullpath = os.path.abspath(title)
    for c in "Your slides are at: %s" % fullpath:
        print(c, end='')
        time.sleep(0.1)
    print()
    print("Opening default web browser")
    time.sleep(0.05)
    webbrowser.open(os.path.join(fullpath, "slides.html"))
    
    
if __name__ == '__main__':
    
    logging.basicConfig(level=logging.DEBUG)
    main()
    
    