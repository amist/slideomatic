import urllib.request
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
    for q in qs:
        try:
            print(q)
        except UnicodeEncodeError:
            print("<<< QUOTE WITH UnicodeEncodeError >>>")

if __name__ == "__main__":
    #subject = "failure"
    #subject = "nature"
    subject = "parents"
    fetch_quotes(subject)