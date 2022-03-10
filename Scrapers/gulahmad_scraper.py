from bs4 import BeautifulSoup
import requests
import urllib.request
import re
import csv
from pprint import pprint


class GulAhmadScraper:

    def __init__(self):

        self.brand = "Gulahmad"
        self.manBaseUrl = 'https://www.gulahmedshop.com/mens-clothes/'
        self.womenBaseUrl = 'https://www.gulahmedshop.com/women/'
        self.kidsBaseUrl = 'https://www.gulahmedshop.com/kids/'

        # Men Categories and subcategories
        self.manCategories = ["western", "eastern"]
        self.manSubCategoriesDict = {
            "eastern": ["gents-kurta", "shalwar-kameez", "president-edition"],
            "western": ["mens-dress-shirts", "mens-casual-shirts"]
        }

        # Women categories and subcategories
        self.womenCategories = ["ideas-pret", "salt", "stitched-fabric"]
        self.womenSubCategoriesDict = {
            "ideas-pret": ["solids", "stitched-suits", "semi-formals", "embroidered", "digitals", ],
            "stitched-fabric": ["suits"],
            "salt": ["tops"]
        }

        # Kids Cateories and subcategories
        self.kidsCategories = ["girls/girls-eastern", "girls/girls-western"]
        self.kidsSubCategoriesDict = {
            "girls/girls-eastern": ["kurtis", "2pc-suits"],
            "girls/girls-western": ["tops"]
        }

    def startScraping(self, genCategory):
        baseUrl = ""
        if genCategory.upper() == "MEN":
            baseUrl = self.manBaseUrl
            print("Scraping Men data from Gulahmad..")
            # products = self.scrapMenData(self.manBaseUrl, genCategory)
        elif genCategory.upper() == "WOMEN":
            baseUrl = self.womenBaseUrl
            print("Scraping women data from Gulahmad..")
            # self.scrapWomenData(self.womenBaseUrl)
        elif genCategory.upper() == "KIDS":
            baseUrl = self.kidsBaseUrl
            print("Scraping Kids data from Gulahmad..")

        products = self.scrapMenData(baseUrl, genCategory)
        return products

    # Start scraping men data
    def scrapMenData(self, baseUrl, genCategory):
        allSubcategoriesProducts = {}

        if genCategory.upper() == "MEN":
            # ********** Man Scraper ****************
            for i in range(len(self.manCategories)):
                URL1 = baseUrl + self.manCategories[i] + "/"

                for j in range(len(self.manSubCategoriesDict[self.manCategories[i]])):
                    URL = URL1 + \
                        self.manSubCategoriesDict[self.manCategories[i]][j] + "?p="
                    print(URL)

                    cat = self.manSubCategoriesDict[self.manCategories[i]][j]
                    productsList = self.orignalScraper(URL, cat)

                    allSubcategoriesProducts[cat] = productsList

        elif genCategory.upper() == "WOMEN":
            # ********** Women Scraper *****************
            for i in range(len(self.womenCategories)):
                URL1 = baseUrl + self.womenCategories[i] + "/"

                for j in range(len(self.womenSubCategoriesDict[self.womenCategories[i]])):
                    URL = URL1 + \
                        self.womenSubCategoriesDict[self.womenCategories[i]][j] + "?p="
                    print(URL)

                    cat = self.womenSubCategoriesDict[self.womenCategories[i]][j]
                    productsList = self.orignalScraper(URL, cat)
                    allSubcategoriesProducts[cat] = productsList

        elif genCategory.upper() == "KIDS":
            # ********** Kids Scraper ******************
            for i in range(len(self.kidsCategories)):
                URL1 = baseUrl + self.kidsCategories[i] + "/"

                for j in range(len(self.kidsSubCategoriesDict[self.kidsCategories[i]])):
                    URL = URL1 + \
                        self.kidsSubCategoriesDict[self.kidsCategories[i]][j] + "?p="
                    print(URL)

                    cat = self.kidsSubCategoriesDict[self.kidsCategories[i]][j]
                    productsList = self.orignalScraper(URL, cat)
                    allSubcategoriesProducts[cat] = productsList

        return allSubcategoriesProducts

    def orignalScraper(self, URL, category):

        x = 1
        productsList = []
        while(x != 2):

            #URL = f'https://www.gulahmedshop.com/mens-clothes?p={x}'
            url1 = 'https:'
            URL = f'{URL}{x}'
            page = requests.get(URL)
            x = x+1
            print(URL)
            soup = BeautifulSoup(page.content, 'html.parser')
            results = soup.find(
                'ol', attrs={'class': 'products list items product-items same-height'})

            job_elems = results.find_all(
                'li', class_='item product product-item')

            # file = open(category+'.csv', 'a+')
            # writer = csv.writer(file)
            # writer.writerow(["imageLink", "productLink", "title",
            #                  "price"])

            # write title row
            # writer.writerow(['Productlinks', 'Title', 'Current Price','Previous Price'])
            job_elems1 = results.find_all(
                'li', class_='item product product-item')
            for job_elem in job_elems:
                title_elem1 = job_elem.find(
                    'span', class_='product-image-wrapper').find('img').get('src')
                # print(title_elem1)
                productlink_elem1 = urllib.parse.urljoin(url1, title_elem1)
                productlink = job_elem.find(
                    'a', class_='product-item-link')
                productlink_elem = productlink['href']
                title_elem = productlink.get_text().strip()
                currentprice_elem = job_elem.find(
                    'span', class_='price').text.strip()

                price = currentprice_elem.split(" ")[1]

                product = {
                    "imageLink": productlink_elem1,
                    "productLink": productlink_elem,
                    "title": title_elem,
                    "price": price,
                    "brand": self.brand
                }

                productsList.append(product)

                # writer.writerow([productlink_elem1, productlink_elem, title_elem,
                #                  currentprice_elem])

            # file.close()

        print("\n")
        return productsList


# scraper = GulAhmadScraper()
# products = scraper.startScraping("Kids")
# pprint(products)
