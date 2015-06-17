import wikipedia
import random

class WikiSentenceGenerator:
    def randomWikiSentence(phrase):
        summ = wikipedia.summary(phrase)
        opts = summ.split(".")
        for i in opts:
            if (random.randint(1,2) == 1):
                return i

        return opts[-1]
