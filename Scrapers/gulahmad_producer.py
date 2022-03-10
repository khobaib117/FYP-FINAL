from producer import Producer
from gulahmad_scraper import GulAhmadScraper


"""
"gents-kurta", "president-edition" => Eid Wear
"shalwar-kameez" => Casual Wear
"mens-dress-shirts" => Formal Wear
"mens-casual-shirts" => casual wear

"solids", "semi-formals" => Formal
"embroidered" => Eid Wear
"digitals", "stitched-suits" => casual wear
"suits" => Party wear
"tops" => Casual

"kurtis", "tops" => casual
"2pc-suits" => formal

"""


class GulahmadProducer:
    def __init__(self):
        self.producerObj = Producer()
        self.categories = ["Men", "Women", "Kids"]
        self.scraper = GulAhmadScraper()

    def publishGulahmadData(self):
        # connect kafka producer
        kafka_producer = self.producerObj.connect_kafka_producer()

        # for each category Men, women and kids scrape data and publish in kafka server
        for i in range(0, len(self.categories), 1):
            # start scraping data from relevent category
            productsDict = self.scraper.startScraping(self.categories[i])
            subcategories = productsDict.keys()

            if self.categories[i].upper() == "MEN":
                # Publish in partition-0
                partition = 0
                topic = ""
                for subcat in subcategories:
                    print("\n", subcat)
                    productsList = productsDict.get(subcat)
                    if subcat == "gents-kurta" or subcat == "president-edition":
                        # Eid Wear
                        topic = "eid-wear"
                    elif subcat == "shalwar-kameez" or subcat == "mens-casual-shirts":
                        # casual wear
                        topic = "casual-wear"
                    elif subcat == "mens-dress-shirts":
                        # Formal wear
                        topic = "formal-wear"

                    for product in productsList:
                        # Publish data in kafka server in key value pairs
                        key = product['title']
                        self.producerObj.publish_message(
                            kafka_producer, topic, key, product, partition)

            elif self.categories[i].upper() == "WOMEN":
                # publish in partition-1
                partition = 1
                topic = ""
                for subcat in subcategories:
                    print("\n", subcat)
                    productsList = productsDict.get(subcat)
                    if subcat == "solids" or subcat == "semi-formals":
                        # Formal Wear
                        topic = "formal-wear"
                    elif subcat == "embroidered":
                        # Eid wear
                        topic = "eid-wear"
                    elif subcat == "digitals" or subcat == "stitched-suits" or subcat == "tops":
                        # Casual wear
                        topic = "casual-wear"
                    elif subcat == "suits":
                        # party wear
                        topic = "party-wear"

                    for product in productsList:
                        # Publish data
                        # print(product)
                        key = product['title']
                        self.producerObj.publish_message(
                            kafka_producer, topic, key, product, partition)

            elif self.categories[i].upper() == "KIDS":
                # publish in partition-2
                partition = 2
                topic = ""
                for subcat in subcategories:
                    print("\n", subcat)
                    productsList = productsDict.get(subcat)
                    if subcat == "kurtis" or subcat == "tops":
                        # Casual Wear
                        topic = "casual-wear"

                    elif subcat == "2pc-suits":
                        # Formal wear
                        topic = "formal-wear"

                    for product in productsList:
                        # Publish data
                        # print(product)
                        key = product['title']
                        self.producerObj.publish_message(
                            kafka_producer, topic, key, product, partition)

            print(
                "\n\n**************************************************************\n\n")


########### MAIN ##############################
producer = GulahmadProducer()
producer.publishGulahmadData()
