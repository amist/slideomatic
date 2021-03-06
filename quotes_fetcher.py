import urllib.request
import random
from bs4 import BeautifulSoup         # pip install beautifulsoup4

class QuotesFetcher(object):
    def fetch_quotes_from_quotationspage(self, subject):
        url = "http://www.quotationspage.com/subjects/%s" % subject
        f = urllib.request.urlopen(url)
        soup = BeautifulSoup(f)
        #quotes = soup.find(class_="quote").find(text=True)      # find one quote
        dts = soup.find_all("dt", class_="quote")
        qs = []
        for dt in dts:
            q = dt.find("a").find(text=True)
            qs.append(q)
            #print(q)
        return qs

    def fetch_quotes_out_of_subject(self, subject):
        qs = self.fetch_quotes_from_quotationspage(subject)
        return qs
        
    def fetch_quotes_out_of_sentence(self, sentence):
        words = sentence.split(" ")
        words.sort(key = lambda s: -len(s))
        index = 0
        if len(words) > 1:
            index = random.randint(0, 1)
        subject = words[index]
        
        print("Using the subject: %s" % subject)
        qs = self.fetch_quotes_out_of_subject(subject)
        
        if len(qs) == 0:
            if index == 0 and len(words) > 1:
                index = 1
            if index == 1:
                index = 0
            subject = words[index]
            print("Using the subject: %s" % subject)
            qs = self.fetch_quotes_out_of_subject(subject)
            
        if (len(qs) == 0):
            qs = [""]
        return qs
        
    def pick_one_quote(self, qs):
        qs.sort(key = lambda s: (len(s) + random.randint(30, 80)))
        #for q in qs:
        #    print("---")
        #    print(q)
        return qs[0]
        


def fetch_quote(sentence):
    if len(sentence) == 0:
        return ""
    qf = QuotesFetcher()
    qs = qf.fetch_quotes_out_of_sentence(sentence)
    return qf.pick_one_quote(qs)

if __name__ == "__main__":
    
    sentence = "How to learn from your mistakes"
    #sentence = "Inspiration is your target"
    
    q = fetch_quote(sentence)
    print(q)
    #print_quotes(qs)