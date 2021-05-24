# KAFKA CLUSTER IN DOCKER WITH MONITORING SYSTEM (GRAFANA + PROMETHEUS)

The lab creates a kafka cluster made up of two functional nodes and a zookeeper manager. It also has monitoring using graphane and prometheus

## Description lab 🚀


The lab does not comply with good practices to be in production. As kafka images we use the ubuntu image so that the kafka installation is not transparent.


### Pre-requisitos 📋

Linux computer with:
* python3
* docker
* docker-compose
* lib-> confluent_kafka (to client python3 producer and consumer)

### Instalación 🔧

- git clone https://github.com/bsotob/kafka.git
- Edit the following property in the files:  advertised.listeners=PLAINTEXT://IP_DOCKER_HOST:909X  

(command to extract it: ip addr show docker0 | grep -Po 'inet \K[\d.]+') and port defined in docker-compose : 9091,9092

          -   kafka_node_1/config/server.properties
          
          -   kafka_node_2/config/server.properties
          
- docker-compose build
- docker-compose up



## Accesos ⚙️

URL access grafana : http://localhost:3000/login

URL access prometheus: http://localhost:9000/targets



