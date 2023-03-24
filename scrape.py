#  The purpose of this file is to contain all scraping abilities of the program.
import string
import urllib
from urllib.request import Request
from bs4 import BeautifulSoup


class Scraper:
    memory = []

    def scrape(self, urls):
        req = Request(url=urls, headers={'User-Agent': 'Mozilla/6.0'})
        with urllib.request.urlopen(req) as f:
            return str(f.read())

    def urlScrape(self, urls):
        soup = BeautifulSoup(self.scrape(urls), 'html.parser')
        obj = soup.find("div", "products row row-small large-columns-4 medium-columns-3 small-columns-2 has-shadow"
                               " row-box-shadow-1 row-box-shadow-3-hover has-equal-box-heights equalize-box")
        even_only = -1
        urlOnPage = []
        for link in obj.find_all('a'):
            even_only += 1
            if even_only % 2 == 0:
                urlOnPage.append(link.get('href'))
            else:
                link.get('href')

        for item in urlOnPage:
            if "?add-to-cart=" in item:
                urlOnPage.remove(item)
        self.memory = urlOnPage
        return urlOnPage

    @staticmethod
    def beautify(lst):
        for item in lst:
            print(item)


class Appliance:
    name = ""
    price = 0
    desc = []
    img = ""
    depth = 0

    def getdepth(self):
        for line in self.desc:
            if 'D-' in line:
                ind = line.index('D-')
                self.depth = line[ind:].strip('″"D- ')

    def listify(self):
        return [self.name, self.price]


class Extractor:
    content_per_url = []
    appliances = []

    def prepare_to_extract(self, lst, limiter):
        """Takes a <List> lst and extracts the very specific data from the URL"""
        scrape = Scraper()
        counter = 0
        for url in lst:
            if counter == limiter:
                break

            counter += 1
            self.content_per_url.append(scrape.scrape(url))
            print(counter)

    def get_details(self, htmlcode):
        soup = BeautifulSoup(htmlcode, 'html.parser')
        name = soup.find("h1", "product-title product_title"
                               " entry-title").getText()[4:]
        price = soup.find("span",
                          "woocommerce-Price-amount amount").find_next("span", "woocommerce-Price-amount"
                                                                               " amount").getText()
        img = soup.find("img").find_next("img").find_next("img").get("src")
        desc = soup.find("div", id="tab-description").find_all("p")
        description = []
        for item in desc:
            description.append(item.getText())
        temp = Appliance()
        temp.name, temp.price, temp.img, temp.desc = name.strip('/'), price, img, description
        self.appliances.append(temp)
        temp.getdepth()

    def testDepth(self, depth):
        for appliance in self.appliances:
            if appliance.depth == depth:
                print(appliance.name, appliance.depth)