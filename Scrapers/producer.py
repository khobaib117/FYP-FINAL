from kafka import KafkaProducer
import kafka
import json
from pprint import pprint
from kafka.errors import KafkaError


class Producer:
    def __init__(self):
        print("")

    def publish_message(self, producer_instance, topic_name, key, value, partition):
        """ Publish message in kafka server in key value pairs"""
        try:
            key_bytes = bytes(key, encoding='utf-8')
            # value_bytes = bytes(value, encoding='utf-8')
            producer_instance.send(
                topic_name, key=key_bytes, value=value, partition=partition)
            producer_instance.flush()
            print('Message published successfully.')
        except Exception as ex:
            print('Exception in publishing message')
            print(str(ex))

    def connect_kafka_producer(self):
        """ Connect producer with kafka server"""
        _producer = None
        try:
            _producer = KafkaProducer(
                bootstrap_servers=['localhost:9092'],
                api_version=(0, 10),
                value_serializer=lambda m: json.dumps(m).encode('ascii'),
                retries=3)

        except Exception as ex:
            print('Exception while connecting Kafka')
            print(str(ex))

        return _producer

    def on_send_success(self, record_metadata):
        print(record_metadata.topic)
        print(record_metadata.partition)
        print(record_metadata.offset)

    def on_send_error(self, excp):
        print("")
        # log.error('I am an errback', exc_info=excp)
        # handle exception
