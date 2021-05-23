FROM ubuntu:latest

RUN apt-get update
RUN apt-get install -y vim wget curl openjdk-8-jdk && wget http://apache.uvigo.es/kafka/2.6.2/kafka-2.6.2-src.tgz && tar zxvf kafka-2.6.2-src.tgz 
RUN mv kafka-2.6.2-src kafka

COPY config/zookeeper.properties /kafka/config/

RUN cd kafka && ./gradlew jar -PscalaVersion=2.13.2  # it needs compile

#CMD /kafka/bin/zookeeper-server-start.sh kafka/config/zookeeper.properties



