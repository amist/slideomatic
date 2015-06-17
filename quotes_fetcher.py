import urllib.request
import random
from bs4 import BeautifulSoup         # pip install beautifulsoup4

def fetch_quotes_from_quotationspage(subject):
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

def fetch_quotes_out_of_subject(subject):
    qs = fetch_quotes_from_quotationspage(subject)
    return qs
    
def fetch_quotes_out_of_sentence(sentence):
    words = sentence.split(" ")
    words.sort(key = lambda s: -len(s))
    index = 0
    if len(words) > 1:
        index = random.randint(0, 1)
    subject = words[index]
    
    print("Using the subject: %s" % subject)
    qs = fetch_quotes_out_of_subject(subject)
    
    if len(qs) == 0:
        if index == 0 and len(words > 1):
            index = 1
        if index == 1:
            index = 0
        subject = words[index]
        print("Using the subject: %s" % subject)
        qs = fetch_quotes_out_of_subject(subject)
        
    if (len(qs) == 0):
        qs = [""]
    return qs
    
def pick_one_quote(qs):
    qs.sort(key = lambda s: (len(s) + random.randint(30, 80)))
    #for q in qs:
    #    print("---")
    #    print(q)
    return qs[0]
    
def print_quotes(qs):
    for q in qs:
        try:
            print(q)
        except UnicodeEncodeError:
            print("<<< QUOTE WITH UnicodeEncodeError >>>")

if __name__ == "__main__":
    sentence = "How to learn from your mistakes"
    qs = fetch_quotes_out_of_sentence(sentence)
    q = pick_one_quote(qs)
    print(q)
    #print_quotes(qs)