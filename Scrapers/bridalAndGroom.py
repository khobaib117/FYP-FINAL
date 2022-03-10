from bs4 import BeautifulSoup
import requests
import urllib.request
import re
import csv
from pprint import pprint


class BridalAndGroom:

    def __init__(self):

        self.brand = "Amir-Adnan"
        self.bridal = 'https://amiradnan.com/women-21/huma-adnan/bridal-collection.html?product_list_limit=all'
        self.groom = 'https://amiradnan.com/wedding-festivities.html?_=1619104514051&is_ajax=1&p='


    def startScraping(self, genCategory):
        productLink = []
        completeProduct = []
        if genCategory.upper() == "GROOM":
            print("Scraping groom data from Amir-Adnan Brand..")
            productLink = []

            for x in range (1, 2):
                r = requests.get (f'https://amiradnan.com/wedding-festivities.html?_=1619104514051&is_ajax=1&p={x}')
                soup = BeautifulSoup(r.content, 'lxml')

                productlist = soup.find_all('li', class_ = 'item product product-item')

                #print (productlist)
                for item in productlist:
                    for link in item.find_all('a', href = True):
                        productLink.append(link['href'])

            for i in productLink:
                if len(i) <= 20:
                    productLink.remove(i)

            mylist = list(dict.fromkeys(productLink))
            for i in mylist:
                if len(i) <= 20:
                    mylist.remove(i)

            for i in mylist:
                print (i)

            for link in mylist:
                r = requests.get(link)
                soup = BeautifulSoup(r.content, 'lxml')
                productName = soup.find('h1', 'page-title').find('span', class_ = 'base').text.strip()
                price = soup.find('div', class_ = 'product-info-price').find('span', class_ = 'price').text.strip()
                imageLink = soup.find('div', class_ = 'product item-image imgzoom').find('img').get('src')
                print ("\n")
                print ("Product Link: " + link)
                print ("Product: " + productName)
                print ("Price: " + price)
                print ("Image Link: " + imageLink)
                print ("Brand: " + self.brand)

                
                completeProductDict = {
                    'productLink' : link,
                    'imageLink' : imageLink,
                    'title' : productName,
                    'price' : price,
                    'brand' : self.brand
                }
                completeProduct.append(completeProductDict)

        elif genCategory.upper() == "BRIDAL":
            print("Scraping Bridal data from Amir-Adnan Brand..")
            productLink = []

            for x in range (1, 2):
                r = requests.get ("https://amiradnan.com/women-21/huma-adnan/bridal-collection.html?product_list_limit=all")
                soup = BeautifulSoup(r.content, 'lxml')

                productlist = soup.find_all('li', class_ = 'item product product-item')

                #print (productlist)
                for item in productlist:
                    for link in item.find_all('a', href = True):
                        productLink.append(link['href'])

            for i in productLink:
                if len(i) <= 20:
                    productLink.remove(i)

            mylist = list(dict.fromkeys(productLink))
            for i in mylist:
                if len(i) <= 20:
                    mylist.remove(i)

            for i in mylist:
                print (i)

            for link in mylist:
                r = requests.get(link)
                productName = soup.find('h1', 'page-title').find('span', class_ = 'base').text.strip()
                price = soup.find('div', class_ = 'product-info-price').find('span', class_ = 'price').text.strip()
                imageLink = soup.find('div', class_ = 'product item-image imgzoom').find('img').get('src')
                print ("\n")
                print ("Product Link: " + link)
                print ("Product: " + productName)
                print ("Price: " + price)
                print ("Image Link: " + imageLink)
                print ("Brand: " + self.brand)

                completeProductDict = {
                    'productLink' : link,
                    'imageLink' : imageLink,
                    'title' : productName,
                    'price' : price,
                    'brand' : self.brand
                }
                completeProduct.append(completeProductDict)
        return completeProduct

scraper = BridalAndGroom()
#products = scraper.startScraping("groom")
products = scraper.startScraping("groom")

print ("\n")
for p in products:
    print(p)
    print('\n')
