from kafkaAdminClient import KafkaAdmin
from producer import Producer
from gulahmad_scraper import GulAhmadScraper


def createTopics():
    kafka_admin_client = KafkaAdmin()
    topicsList = ["bridal-wear", "groom-wear",
                  "party-wear", "eid-wear", "casual-wear", "formal-wear"]

    """
    partition-0: Men
    partition-1: Women
    partition-2: Kids
    """
    partitions = 3
    replication = 1
    kafka_admin_client.createTopics(topicsList, partitions, replication)

    # kafka_admin_client.deleteTopicsFromCluster(topicsList)
    kafka_admin_client.close()


def main():
    print("1. Create Topics and partitions\n2. Publish data into kafka broker")
    selection = input("Enter your choice: ")
    if selection == "1":
        # Create topics and partitions
        createTopics()

    elif selection == "2":
        producerObj = Producer()
        kafka_producer = producerObj.connect_kafka_producer()

        topic = ""
        key = ""
        value = ""
        partition = 0

        producerObj.publish_message(
            kafka_producer, topic, key, value, partition)

        if kafka_producer is not None:
            kafka_producer.close()


######################## MAIN ##########################################
main()
