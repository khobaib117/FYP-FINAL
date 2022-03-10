
from kafka import KafkaProducer
import kafka
import json
from pprint import pprint
from kafka.errors import KafkaError
from producer import Producer
# **************************** TEST Producer ************************************************
price = 1000
product = {
    "imageLink": "Sample image link",
    "productLink": "Sample product link",
    "title": "First title",
    "price": str(price),
    "brand": "Gulahmad"
}
producerObj = Producer()
kafka_producer = producerObj.connect_kafka_producer()

for i in range(10):
    price += 1000
    product['price'] = str(price)
    producerObj.publish_message(
        kafka_producer, "test", product['title'], product, 0)

    product['title'] = "third title"

if kafka_producer is not None:
    kafka_producer.close()
