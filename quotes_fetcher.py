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

def fetch_quotes(subject):
    qs = fetch_quotes_from_quotationspage(subject)
    return qs
    
def print_quotes(qs):
    for q in qs:
        try:
            print(q)
        except UnicodeEncodeError:
            print("<<< QUOTE WITH UnicodeEncodeError >>>")

if __name__ == "__main__":
    sentence = "How to learn from your mistakes"
    words = sentence.split(" ")
    #longest_word = max(words, key=len)
    words.sort(key = lambda s: -len(s))
    index = 0
    if len(words) > 1:
        index = random.randint(0, 1)
    subject = words[index]
    #subject = longest_word
    #subject = "failure"
    #subject = "nature"
    #subject = "parents"
    print("Using the subject: %s" % subject)
    qs = fetch_quotes(subject)
    if len(qs) == 0:
        if index == 0 and len(words > 1):
            index = 1
        if index == 1:
            index = 0
        subject = words[index]
        print("Using the subject: %s" % subject)
        qs = fetch_quotes(subject)
    print_quotes(qs)