from urllib.request import urlopen
import sys

def countWord(url):
    d = dict()
    with urlopen(url) as web_f:
        for line in web_f:
            for word in line.decode().split():
                d[word] = d.get(word,0) + 1
    return d

def display_sorted_dict(d):
    d = dict(zip(d.values(),d.keys()))
    for k, item in sorted(d.items(), reverse=True):
        print(f"{k}: {item}" )

if __name__ == '__main__':
    url = sys.argv[1]
    d = countWord(url)
    display_sorted_dict(d)