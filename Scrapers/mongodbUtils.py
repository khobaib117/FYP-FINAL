import pymongo
from pprint import pprint
# from gulahmad_scraper import GulAhmadScraper
import json
import datetime


class MongoDbHandler:
    def __init__(self):
        print("")

    def connectDb(self, user, password, database):
        """connect to MongoDB"""

        self.dbClient = pymongo.MongoClient(
            f'mongodb://{user}:{password}@cluster0-shard-00-00.4s7gf.mongodb.net:27017,cluster0-shard-00-01.4s7gf.mongodb.net:27017,cluster0-shard-00-02.4s7gf.mongodb.net:27017/{database}?ssl=true&replicaSet=atlas-ucptyb-shard-0&authSource=admin&retryWrites=true&w=majority'
        )
        # f'mongodb://scott:root123@cluster0-shard-00-00.4s7gf.mongodb.net:27017,cluster0-shard-00-01.4s7gf.mongodb.net:27017,cluster0-shard-00-02.4s7gf.mongodb.net:27017/shopspot?ssl=true&replicaSet=atlas-ucptyb-shard-0&authSource=admin&retryWrites=true&w=majority')
        self.db = self.dbClient.shopspot

        # Issue the serverStatus command and print the results
        serverStatusResult = self.db.command("serverStatus")
        print("\n*********************** DB CONNECTION STATUS ****************************************************\n")
        pprint(serverStatusResult)
        print("\n*************************************************************************************************\n")

    def insertOne(self, collection, product):
        """ Insert a single product into db"""

        # get collection
        collection = self.db[collection]
        # insert one product
        insertedRecord = collection.insert_one(product)
        # return id of inserted record
        return insertedRecord.inserted_id

    def insertAll(self, collection, productsList):
        """ Insert a List of products into db"""
        # get Collection
        collection = self.db[collection]
        # Insert all products into the db
        insertedRecords = collection.insert_many(productsList)

        # return list of ids of all inserted objects
        return insertedRecords.inserted_ids

    def findAll(self, collection):
        """Retrieve all products from a collection"""
        # get Collection
        collection = self.db[collection]
        # Retrieve all records
        productsCursor = collection.find({})

        productsList = []
        if productsCursor.count() > 0:
            for product in productsCursor:
                productsList.append(product)

        return productsList

    def findByTitle(self, collection, title):
        # get Collection
        collection = self.db[collection]
        productsCursor = collection.find({"title": title})

        productsList = []
        if productsCursor.count() > 0:
            for product in productsCursor:
                productsList.append(product)

        return productsList

    def findOneByTitleAndReplace(self, collection, title, newProduct):
        """ Find a product by title, if found replace it with new
            product, else add a new document with new product """

        # get Collection
        collection = self.db[collection]

        product = collection.find_one_and_replace(
            {"title": title},
            newProduct,
            return_document=pymongo.ReturnDocument.AFTER,
            upsert=True)

        # return updated product
        return product

    def closeDbConnection(self):
        self.dbClient.close()


# mongodb = MongoDbHandler()
# mongodb.connectDb(dbUsername, dbPassword, databaseName)
