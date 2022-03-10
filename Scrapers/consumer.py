import json
from time import sleep
from kafka import KafkaConsumer
from pprint import pprint
from mongodbUtils import MongoDbHandler
import datetime

if __name__ == '__main__':

    dbUsername = ""     # add mongodb username here
    dbPassword = ""     # mongodb passowrd
    databaseName = ""   # database name
    mongodb = MongoDbHandler()
    mongodb.connectDb(dbUsername, dbPassword, databaseName)

    # Topics list in kafka broker
    topicsList = ["bridal-wear", "groom-wear",
                  "party-wear", "eid-wear", "casual-wear", "formal-wear"]

    # get all events and categories from db
    eventsList = mongodb.findAll("events")
    categoryList = mongodb.findAll("categories")

    eventsDict = {}
    categoriesDict = {}

    # save events in event: id pair
    for event in eventsList:
        eventsDict[event["event"]] = event["_id"]

    # save category in categoryname: id pair
    for cat in categoryList:
        categoriesDict[cat["name"]] = cat["_id"]

    pprint(eventsDict)
    pprint(categoriesDict)

    # consume data from each topic one by one
    for topic in topicsList:
        print("Loading data from the topic: ", topic)
        consumer = KafkaConsumer(topic, auto_offset_reset='earliest',
                                 bootstrap_servers=['localhost:9092'],
                                 api_version=(0, 10), consumer_timeout_ms=1000,
                                 enable_auto_commit=False)

        collection = "products"
        # event id that is stored in db correspond to event
        eventId = eventsDict[topic]
        categoryId = ""

        count = 0
        for message in consumer:
            product = {}
            # load single product from kafka as json object
            product = json.loads(message.value)
            partition = message.partition   # get partition in topic

            if partition == 0:
                # set cateory as Men
                categoryId = categoriesDict["man"]
                print(" In Partition ", partition)

            if partition == 1:
                # set category as women
                categoryId = categoriesDict["women"]
                print(" In Partition ", partition)

            if partition == 2:
                # set category as Kid
                categoryId = categoriesDict["kid"]
                print(" In Partition ", partition)

            # remove illegal characters from title to avoid inconvenience
            # Create a complete json object to push in mongodb
            product['title'] = product['title'].replace("/", "-")
            product['title'] = product['title'].replace("\\", "-")
            product['title'] = product['title'].replace("|", "-")
            product['title'] = product['title'].replace("<", " ")
            product['title'] = product['title'].replace(">", " ")
            product['title'] = product['title'].replace("'", "")
            product["category"] = categoryId
            product["event"] = eventId
            product["createdAt"] = datetime.datetime.utcnow()
            product["updatedAt"] = datetime.datetime.utcnow()

            # insert product into db
            mongodb.findOneByTitleAndReplace(
                collection, product["title"], product)

            pprint(product)
            count += 1
            print('\n')

        print("Total Records Added in Database: ", count)
        print("\n\n*****************************************************************\n\n")

    if consumer is not None:
        consumer.close()

    mongodb.closeDbConnection()  # close database connection
