import wikipedia
import random
from concurrent.futures import ThreadPoolExecutor
import logging
log = logging.getLogger('pop')

MAX_WORKERS = 12

def get_wiki_summary(phrase):
    summ = []
    log.info ("pharse=%s", phrase)
    try:
        summ.append(wikipedia.summary(phrase).split('. ')[0])
    except wikipedia.exceptions.PageError:
        
        words = phrase.split()
        log.debug("words=%s", words)
        if len(words) < 2:
            log.info('WAT')
            return []
        else:
            log.debug('popcorn')
            ex = ThreadPoolExecutor(max_workers=MAX_WORKERS)
                #summ += list(ex.map(get_wiki_summary, phrase.split()))
            log.debug ("checking")
            summ += list(ex.map(get_wiki_summary, phrase.split(' ')))
            log.debug("checked")
            if len(summ) == 0:
                print("got nothing...")
                return []
            log.debug('blah')
                
            
    except wikipedia.exceptions.DisambiguationError as e:
        suggestions = format(str(e)).split("\n")[1:-1]
        log.debug('suggestions=%s', suggestions)
        #summ = get_wiki_summary(suggestions[random.randint(0, len(suggestions))])
        summ += get_wiki_summary(suggestions[0])
    finally:
        return summ
    
def random_wiki_sentence(phrase):
    summ = get_wiki_summary(phrase)
    
    #print("opts = " + format(str(opts)) + "\n")
    #for i in opts:        
    #    if i and random.random() < 0.3:
    #        return i
    return random.choice(summ)

if __name__ == '__main__':
    logging.basicConfig(level=0)
    print(random_wiki_sentence('not like toads who suck balls'))
