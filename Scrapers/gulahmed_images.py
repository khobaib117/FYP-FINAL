from bs4 import BeautifulSoup
import requests
import urllib.request
import re
import csv
import pathlib
import os


class GulAhmadScraper:

    def __init__(self):
        self.manBaseUrl = 'https://www.gulahmedshop.com/mens-clothes/'
        self.womenBaseUrl = 'https://www.gulahmedshop.com/women/'
        self.kidsBaseUrl = 'https://www.gulahmedshop.com/kids/'

        # Men Categories and subcategories
        self.manCategories = ["western", "eastern"]
        self.manSubCategoriesDict = {
            "eastern": ["gents-kurta", "shalwar-kameez", "president-edition"],
            "western": ["mens-dress-shirts", "mens-casual-shirts"]
        }

        # Woemn categories and subcategories
        self.womenCategories = ["ideas-pret", "salt"]
        self.womenSubCategoriesDict = {
            "ideas-pret": ["solids", "stitched-suits", "formals"],
            "salt": ["sweaters", "tops"]
        }

        # Kids Cateories and subcategories
        self.kidsCategories = []
        self.kidsSubCategoriesDict = {
            "eastern": [],
            "western": []
        }

    def startScraping(self, genCategory):
        baseUrl = ""
        if genCategory == "Men":
            print("Scraping Men data from Gulahmad..")
            self.scrapMenData(self.manBaseUrl)
        elif genCategory == "women":
            baseUrl = self.womenBaseUrl
            print("Scraping women data from Gulahmad..")
            self.scrapWomenData(self.womenBaseUrl)
        elif genCategory == "Kids":
            baseUrl = self.kidsBaseUrl
            print("Scraping Kids data from Gulahmad..")

    # Start scraping men data
    def scrapMenData(self, baseUrl):
        for i in range(len(self.manCategories)):
            URL1 = baseUrl + self.manCategories[i] + "/"

            for j in range(len(self.manSubCategoriesDict[self.manCategories[i]])):
                URL = URL1 + \
                    self.manSubCategoriesDict[self.manCategories[i]][j] + "?p="
                print(URL)

                cat = self.manSubCategoriesDict[self.manCategories[i]][j]
                self.orignalScraper(URL, cat)

        # Start scraping women data
    def scrapWomenData(self, baseUrl):
        for i in range(len(self.womenCategories)):
            URL1 = baseUrl + self.womenCategories[i] + "/"

            for j in range(len(self.womenSubCategoriesDict[self.womenCategories[i]])):
                URL = URL1 + \
                    self.womenSubCategoriesDict[self.womenCategories[i]][j] + "?p="
                print(URL)

                cat = self.womenSubCategoriesDict[self.womenCategories[i]][j]
                self.orignalScraper(URL, cat)

    def orignalScraper(self, URL, category):

        x = 1
        while(x != 2):

            #URL = f'https://www.gulahmedshop.com/mens-clothes?p={x}'
            url1 = 'https:'
            print("In Orignal scraper")
            URL = f'{URL}{x}'
            page = requests.get(URL)
            x = x+1
            print(URL)
            soup = BeautifulSoup(page.content, 'html.parser')
            results = soup.find(
                'ol', attrs={'class': 'products list items product-items same-height'})

            # print(results.prettify())

            job_elems = results.find_all(
                'li', class_='item product product-item')

            for job_elem in job_elems:
                title_elem = job_elem.find(
                    'span', class_='product-image-wrapper').find('img').get('src')
                print(title_elem)
                productlink_elem = urllib.parse.urljoin(url1, title_elem)
                print(productlink_elem)
                nametemp = job_elem.find('img').get('alt')
                if len(nametemp) == 0:
                    filename = str(i)
                    i = i+1
                else:
                    filename = nametemp

                wpath = pathlib.Path(__file__).parent.absolute()
                spath = category
                path = os.path.join(wpath, spath)
                if not os.path.exists(path):
                    os.makedirs(path)
                os.chdir(path)

                imagefile = open(filename+".jpg", 'wb')
                imagefile.write(urllib.request.urlopen(
                    productlink_elem).read())
                imagefile.close()


scraper = GulAhmadScraper()
scraper.startScraping("Men")
scraper.startScraping("women")
