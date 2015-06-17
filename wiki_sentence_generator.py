import wikipedia
import random

def get_wiki_summary(phrase):
    summ = ""
    try:
        summ = wikipedia.summary(phrase)
    except wikipedia.exceptions.PageError:
        words = phrase.split(" ")
        if len(words) < 2:
            return ""
        else:
            for word in phrase.split(" "):
                answer = get_wiki_summary(word).split(".")[0]
                if answer:
                    summ += "." + get_wiki_summary(word).split(".")[0]
    except wikipedia.exceptions.DisambiguationError as e:
        suggestions = format(str(e)).split("\n")[1:-1]
        #summ = get_wiki_summary(suggestions[random.randint(0, len(suggestions))])
        summ = get_wiki_summary(suggestions[0])
    finally:
        return summ
    
def random_wiki_sentence(phrase):
    summ = get_wiki_summary(phrase)
    
    opts = summ.split(". ")
    for i in opts:        
        if i and random.random() < 0.5:
            return i

    return opts[0]
