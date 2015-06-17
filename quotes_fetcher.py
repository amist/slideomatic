import urllib.request
from bs4 import BeautifulSoup         # pip install beautifulsoup4

#base_url_1 = "http://www.brainyquote.com/quotes/topics/topic_%s.html"      # forbidden

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
    for q in qs:
        print(q)

if __name__ == "__main__":
    subject = "failure"
    fetch_quotes(subject)