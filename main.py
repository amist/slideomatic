'''
Created on Jun 17, 2015

@author: yglazner
'''
import core
from core import BACKENDS
import logging

def inp_m(s):
    lines = [inp(s)]
    line = '*'
    while line:
        line = input("more:\n")
        lines.append(line)
        
    return "\n".join(lines[:-1])
        

def inp(s):
    a = ''
    while not a.strip():
        a = input(s)
        with open('lastrun', 'a') as f:
            f.write(a+"\n")
       
        
    return a.strip()

def main():
    print("Welcome!\n")
    with open('lastrun' ,'wb'): 
        pass
    title = inp("Title:\n")
    
    author = inp("Author:\n")
    paragraphs = []
    for i in range(1, 2000):
        para = inp("Insert text for slide %d(q to quit):"%i)
        if para.strip() in 'qQ':
            break
        line = '*'
        while 1:
            line = input("more:\n")
            if not line: break
            para += '\n' + line
    
        paragraphs.append(para)
    backend = ''
    while backend not in BACKENDS:
        backend = inp("Backend [%s]:\n"% ", ".join(BACKENDS.keys()))
        
    core.generate(title, author, paragraphs, backend)
    print ("Woo hooy!")
    
if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    main()
    
    