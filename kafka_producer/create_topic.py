from confluent_kafka import Producer
import socket

conf = {'bootstrap.servers': "localhost:9092"}

producer = Producer(conf)


producer.produce("NEW_TOPIC", key="key_name" , value="value_name")

producer.flush()

