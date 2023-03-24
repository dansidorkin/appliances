import urllib.request
from urllib.request import Request
import scrape


def store(name, urls, appliance):
    strippedname = name.replace('/','-')
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    urllib.request.install_opener(opener)
    urllib.request.urlretrieve(urls, strippedname + ".jpg")

    with open(strippedname + '.txt', 'w') as f:
        for item in appliance.listify():
            f.write(item + "\n")
        for item in appliance.desc:
            f.write(item + '\n')
    f.close()