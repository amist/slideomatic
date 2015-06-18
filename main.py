'''
Created on Jun 17, 2015

@author: yglazner
'''
import core
from core import BACKENDS
import logging
        
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
    print ("Woo hooy!")
    
if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    main()
    
    