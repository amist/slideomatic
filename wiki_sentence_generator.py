import wikipedia
import random
from concurrent.futures import ThreadPoolExecutor
import logging
import itertools
log = logging.getLogger('pop')

#from nltk.tag import pos_tag

MAX_WORKERS = 12

def get_wiki_summary(phrase):
    summ = []
    log.info ("pharse=%s\n", phrase)
    try:
        sentence = wikipedia.summary(phrase).split('. ')[0]
        log.debug("got: %s\n", sentence)
        summ.append(sentence)
    except wikipedia.exceptions.PageError:
        log.debug("exepted!!\n")  
        if len(phrase.split()) < 2:
            log.debug("WAT=\n")    
            return []
        
        words = [w for w in phrase.split() if len(w)>3]
        log.debug("words=%s\n", words)
        if len(words) < 1:
            return []
        else:
            log.debug('popcorn')
            ex = ThreadPoolExecutor(max_workers=MAX_WORKERS)
                #summ += list(ex.map(get_wiki_summary, phrase.split()))
            log.debug("summ before is: %s\n", summ)
            
            summ += list(itertools.chain(*ex.map(get_wiki_summary, words)))

            log.debug("summ is now: %s\n", summ)
            return summ    
            
    except wikipedia.exceptions.DisambiguationError as e:
        log.debug("excepted\n")  
        suggestions = format(str(e)).split("\n")[1:-1]
        log.debug('suggestions=%s', suggestions)
        #summ = get_wiki_summary(suggestions[random.randint(0, len(suggestions))])
        summ += get_wiki_summary(suggestions[0])
    finally:
        return summ
    
def random_wiki_sentence(phrase):
    summ = get_wiki_summary(phrase)
    log.debug("\n\nsumm=%s\n\n", summ)
    
    #print("opts = " + format(str(opts)) + "\n")
    for i in summ:        
        if i and random.random() < 0.5:
            return i
    return summ[0]

    #return random.choice(summ)

if __name__ == '__main__':
    logging.basicConfig(level=0)
    print(random_wiki_sentence('ford\nis a car'))
