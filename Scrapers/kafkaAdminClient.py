from kafka import KafkaAdminClient, admin
import json

"""Kafka Admon client to manage kafka server, creating topics and partitions"""


class KafkaAdmin:
    def __init__(self):
        # get instance of kafka admin client
        self.adminClient = KafkaAdminClient(
            bootstrap_servers=['localhost:9092'], api_version=(0, 10))

    def createTopics(self, topicsNameList, numPartitions, replicationFactor):
        """ Create the topics in kafka server with 3 partitions(Men, Women, Kids) each """
        try:
            topics = []
            topicConfigs = {
                # 'delete.retention.ms': '100',
                'cleanup.policy': 'compact',
                # 'segment.ms': '100',
                # 'min.cleanable.dirty.ratio': '0.01'
            }
            for topic_name in topicsNameList:
                if topic_name.upper() == "BRIDAL-WEAR" or topic_name.upper() == "GROOM-WEAR":
                    numPartitions = 1

                # create new topic with 3 partitions
                topic = admin.NewTopic(
                    name=topic_name, num_partitions=numPartitions, replication_factor=replicationFactor,
                    topic_configs=topicConfigs)
                topics.append(topic)
                numPartitions = 3

            self.adminClient.create_topics(topics)
        except Exception as ex:
            print(ex)

    def createPartition(self, topic, numPartitions):
        """Create partions in the topic"""
        part = admin.NewPartitions(numPartitions)
        m = {
            topic: part
        }
        self.adminClient.create_partitions(m)

    def deleteTopicsFromCluster(self, topicsList):
        """Delete all topics from kafka cluster"""
        self.adminClient.delete_topics(topicsList, 6000)

    def close(self):
        """ Destroy admin client instance and close connection with kafka server"""
        self.adminClient.close()
