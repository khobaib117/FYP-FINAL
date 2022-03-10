from producer import Producer
from jdot_scraper import JunaidJamshaidScraper


"""
"kameez-shalwar/semi-formal", "kameez-shalwar/formal" => Formal Wear
"kameez-shalwar/casual", "kurta/casual", "kurta/semi-formal" => Casual Wear
"kameez-shalwar/exclusive", "kurta/formal" => eid wear
"grooms-collection/prince-coat", "grooms-collection/sherwani" => groom wear
 
"kurti/designer-kurti" => party wear 
"kurti/casual-printed-kurti" => casual wear

"kids-boys/kameez-shalwar" => casual
 "kids-boys/kurta", "teen-boys/kameez-shalwar"  => eid wear
"teen-boys/special-kurta" => party wear
"teen-girls/stitched-collection", "teen-girls/kurti" => party wear

"""


class JdotProducer:
    def __init__(self):
        self.producerObj = Producer()
        self.categories = ["Men", "Women", "Kids"]
        self.scraper = JunaidJamshaidScraper()

    def publishJdotData(self):
        kafka_producer = self.producerObj.connect_kafka_producer()

        for i in range(0, len(self.categories), 1):
            productsDict = self.scraper.startScraping(self.categories[i])
            subcategories = productsDict.keys()

            if self.categories[i].upper() == "MEN":
                # Publish in partition-0
                partition = 0
                topic = ""
                for subcat in subcategories:
                    print("\n", subcat)
                    productsList = productsDict.get(subcat)
                    if subcat == "kameez-shalwar/exclusive" or subcat == "kurta/formal":
                        # Eid Wear
                        topic = "eid-wear"
                    elif subcat == "kameez-shalwar/casual" or subcat == "kurta/casual" or subcat == "kurta/semi-formal":
                        # casual wear
                        topic = "casual-wear"
                    elif subcat == "kameez-shalwar/semi-formal" or subcat == "kameez-shalwar/formal":
                        # Formal wear
                        topic = "formal-wear"

                    for product in productsList:
                        # Publish data
                        # print(product)
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

                    if subcat == "kurti/casual-printed-kurti":
                        # Casual wear
                        topic = "casual-wear"
                    elif subcat == "kurti/designer-kurti":
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
                    if subcat == "kids-boys/kameez-shalwar":
                        # Casual Wear
                        topic = "casual-wear"

                    elif subcat == "kids-boys/kurta" or subcat == "teen-boys/kameez-shalwar":
                        topic = "eid-wear"

                    elif subcat == "teen-boys/special-kurta" or subcat == "teen-girls/stitched-collection" or subcat == "teen-girls/kurti":
                        topic = "party-wear"

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
producer = JdotProducer()
producer.publishJdotData()
