from bs4 import BeautifulSoup
import requests
import urllib.request
import re
import csv
from pprint import pprint


class JunaidJamshaidScraper:

    def __init__(self):

        self.brand = "Junaid Jamshaid"
        self.manBaseUrl = 'https://www.junaidjamshed.com/mens/'
        self.womenBaseUrl = 'https://www.junaidjamshed.com/womens/'
        self.kidsBaseUrl = 'https://www.junaidjamshed.com/boys-girls/'

        # Men Categories and subcategories
        self.manCategories = ["kameez-shalwar", "kurta", "grooms-collection"]
        self.manSubCategoriesDict = {
            "kameez-shalwar": ["casual", "semi-formal", "formal", "exclusive"],
            "kurta": ["casual", "semi-formal", "formal"],
            "grooms-collection": ["prince-coat", "sherwani"]
        }

        # Women categories and subcategories
        self.womenCategories = ["kurti"]
        self.womenSubCategoriesDict = {
            "kurti": ["designer-kurti", "casual-printed-kurti"]
        }

        # Kids Cateories and subcategories
        self.kidsCategories = ["kids-boys", "teen-boys", "teen-girls"]
        self.kidsSubCategoriesDict = {
            "kids-boys": ["kameez-shalwar", "kurta"],
            "teen-boys": ["special-kurta", "kameez-shalwar"],
            "teen-girls": ["stitched-collection", "kurti"]
        }

    def startScraping(self, genCategory):
        baseUrl = ""
        products = []
        if genCategory.upper() == "MEN":
            baseUrl = self.manBaseUrl
            print("Scraping Men data from Junaid Jamshaid..")
            # products = self.scrapMenData(self.manBaseUrl, genCategory)
        elif genCategory.upper() == "WOMEN":
            baseUrl = self.womenBaseUrl
            print("Scraping women data from Junaid Jamshaid..")
            # self.scrapWomenData(self.womenBaseUrl)
        elif genCategory.upper() == "KIDS":
            baseUrl = self.kidsBaseUrl
            print("Scraping Kids data from Junaid Jamshaid..")

        products = self.scrapMenData(baseUrl, genCategory)
        return products

    # Start scraping men data
    def scrapMenData(self, baseUrl, genCategory):
        allSubcategoriesProducts = {}

        if genCategory.upper() == "MEN":
            # **** Man Scraper ******
            for i in range(len(self.manCategories)):
                URL1 = baseUrl + self.manCategories[i] + "/"

                for j in range(len(self.manSubCategoriesDict[self.manCategories[i]])):
                    URL = URL1 + \
                        self.manSubCategoriesDict[self.manCategories[i]
                                                  ][j] + ".html?p="
                    print(URL)

                    mainCat = self.manCategories[i]
                    subcat = self.manSubCategoriesDict[self.manCategories[i]][j]
                    cat = ""+mainCat+"/"+subcat
                    productsList = self.orignalScraper(URL, cat)

                    allSubcategoriesProducts[cat] = productsList

        elif genCategory.upper() == "WOMEN":
            # **** Women Scraper *******
            for i in range(len(self.womenCategories)):
                URL1 = baseUrl + self.womenCategories[i] + "/"

                for j in range(len(self.womenSubCategoriesDict[self.womenCategories[i]])):
                    URL = URL1 + \
                        self.womenSubCategoriesDict[self.womenCategories[i]
                                                    ][j] + ".html?p="
                    print(URL)

                    mainCat = self.womenCategories[i]
                    subcat = self.womenSubCategoriesDict[self.womenCategories[i]][j]
                    cat = ""+mainCat+"/"+subcat

                    productsList = self.orignalScraper(URL, cat)
                    allSubcategoriesProducts[cat] = productsList

        elif genCategory.upper() == "KIDS":
            # **** Kids Scraper ******
            for i in range(len(self.kidsCategories)):
                URL1 = baseUrl + self.kidsCategories[i] + "/"

                for j in range(len(self.kidsSubCategoriesDict[self.kidsCategories[i]])):
                    URL = URL1 + \
                        self.kidsSubCategoriesDict[self.kidsCategories[i]
                                                   ][j] + ".html?p="
                    print(URL)

                    mainCat = self.kidsCategories[i]
                    subcat = self.kidsSubCategoriesDict[self.kidsCategories[i]][j]
                    cat = ""+mainCat+"/"+subcat
                    productsList = self.orignalScraper(URL, cat)
                    allSubcategoriesProducts[cat] = productsList

        return allSubcategoriesProducts

    def orignalScraper(self, URL, category):
        completeProduct = []
        x = 1
        while(x != 2):

            #URL = f'https://www.gulahmedshop.com/mens-clothes?p={x}'
            url1 = 'https:'
            URL = f'{URL}{x}'
            page = requests.get(URL)
            x = x+1
            print(URL)

            soup = BeautifulSoup(page.content, 'html.parser')
            productLink = []

            productlist = soup.find_all(
                'li', class_='item product product-item')

            for item in productlist:
                for link in item.find_all('a', href=True):
                    productLink.append(link['href'])

            for i in productLink:
                if len(i) <= 20:
                    productLink.remove(i)

            mylist = list(dict.fromkeys(productLink))
            for i in mylist:
                if len(i) <= 20:
                    mylist.remove(i)

            for i in mylist:
                print(i)

            for link in mylist:
                r = requests.get(link)
                soup = BeautifulSoup(r.content, 'html.parser')
                productName = soup.find(
                    'h1', class_='page-title').find('span', class_='base').text.strip()
                price = soup.find(
                    'div', class_='price-box price-final_price').find('span', class_='price').text.strip()
                imageLink = soup.find(
                    'div', class_='MagicToolboxContainer selectorsBottom minWidth').find('img').get('src')

                completeProductDict = {
                    'productLink': link,
                    'imageLink': imageLink,
                    'title': productName,
                    'price': price,
                    'brand': self.brand
                }
                completeProduct.append(completeProductDict)
                # print (productName, price)
        return completeProduct


# scraper = JunaidJamshaidScraper()
# products = scraper.startScraping("Women")
# pprint(products)
# for p in products:
#     print(p)
#     print('\n')
# scraper.startScraping("women")
