# KAFKA CLUSTER IN DOCKER WITH MONITORING SYSTEM (GRAFANA + PROMETHEUS)

The lab creates a kafka cluster made up of two functional nodes and a zookeeper manager. It also has monitoring using graphane and prometheus

## Description lab 🚀


The lab does not comply with good practices to be in production. As kafka images we use the ubuntu image so that the kafka installation is not transparent.


### Pre-requisitos 📋

Linux computer with:
* python3
* docker
* docker-compose
* lib-> confluent_kafka (to client python3 producer and consumer) -> pip3 install confluent-kafka

### Instalación 🔧

- git clone https://github.com/bsotob/kafka.git
- Edit the following property in the files:  advertised.listeners=PLAINTEXT://IP_DOCKER_HOST:909X  

(command to extract it: ip addr show docker0 | grep -Po 'inet \K[\d.]+') and port defined in docker-compose : 9091,9092

          -   kafka_node_1/config/server.properties
          
          -   kafka_node_2/config/server.properties
          
          exemple: "advertised.listeners=PLAINTEXT://172.17.0.1:9092"
          
- docker-compose build
- docker-compose up

## KAFKA Producer TESTING

```
python3 kafka_producer/create_topic.py

```

code python client:


```

from confluent_kafka import Producer
import socket

conf = {'bootstrap.servers': "localhost:9092"}

producer = Producer(conf)


producer.produce("fruteria_topic", key="fruta" , value="mamanzana")

producer.flush()


```
## KAFKA Consumer TESTING

```
python3 kafka_consumer/consumer_topic.py

```

code python client:


```

from confluent_kafka import Consumer

c = Consumer({
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'mygroup',
    'auto.offset.reset': 'earliest'
})

c.subscribe(['fruteria_topic'])

while True:
    msg = c.poll(1.0)

    if msg is None:
        continue
    if msg.error():
        print("Consumer error: {}".format(msg.error()))
        continue

    print('Received message: {}'.format(msg.value().decode('utf-8')))

c.close()


```

## urls access

URL access grafana : http://localhost:3000/login

![Alt text](https://github.com/bsotob/kafka/blob/main/grafana.JPG)
https://github.com/bsotob/kafka/blob/main/grafana.JPG

URL access prometheus: http://localhost:9000/targets


