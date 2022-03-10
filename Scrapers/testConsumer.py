import json
from time import sleep
from kafka import KafkaConsumer
from pprint import pprint
from mongodbUtils import MongoDbHandler
import datetime


mongodb = MongoDbHandler()
mongodb.connectDb("scott", "root123", "shopspot")

# print("Loading data from the topic: test")
consumer = KafkaConsumer("test", auto_offset_reset='earliest',
                         bootstrap_servers=['localhost:9092'],
                         api_version=(0, 10), consumer_timeout_ms=1000,
                         enable_auto_commit=False)

count = 0
for message in consumer:
    record = json.loads(message.value)
    print(record)
    mongodb.findOneByTitleAndReplace("test", record['title'], record)
    count += 1
    print('\n')

print("Message COUNT: ", count)
print("\n\n*****************************************************************\n\n")
if consumer is not None:
    consumer.close()
