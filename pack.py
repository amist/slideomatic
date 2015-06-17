'''
Created on Jun 18, 2015

@author: yglazner
'''
import sys
import os
import shutil




def main(name):
    if os.path.isdir(name):
        print ("folder", name, "exists")
        return
    os.mkdir(name)
    p = lambda s: os.path.join(name, s)
    def cptree(folder):
        shutil.copytree(folder, p(folder))
    cptree("images")
    cptree('impress')
    shutil.copy('slides.html', p('slides.html'))
    


if __name__ == '__main__':
    assert len(sys.argv)==2, 'Usage NAME'
    main(sys.argv[1])