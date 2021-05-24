from confluent_kafka import Producer
import socket

conf = {'bootstrap.servers': "0.0.0.0:9092"}

producer = Producer(conf)


producer.produce("ropa", key="bamba" , value="nike")

producer.flush()

