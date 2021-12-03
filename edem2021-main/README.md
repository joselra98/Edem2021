# Kafka - Lab 0 

## Objectives

 1) Run Zookeeper + Kafka
 2) Check status
 3) Create a topic

## Run
Simple scenario: 1 zookeeper + 1 Kafka broker.

Start the ZooKeeper and Kafka container.

```sh
$ docker-compose up -d
```

Status: 

```sh
$ docker-compose ps
      Name                  Command            State                     Ports
-------------------------------------------------------------------------------------------------
lab0_kafka_1       /etc/confluent/docker/run   Up      0.0.0.0:9092->9092/tcp
lab0_zookeeper_1   /etc/confluent/docker/run   Up      0.0.0.0:2181->2181/tcp, 2888/tcp, 3888/tcp
```


### Create Topic

Create a topic named `myTopic`, one partition and one replica.

```sh
$ docker-compose exec kafka kafka-topics --create --topic myTopic --partitions 1 --replication-factor 1 --if-not-exists --bootstrap-server host.docker.internal:9092
```

Output: 

```sh
Created topic myTopic.
```

Topic information:

```sh
$ docker-compose exec kafka kafka-topics --describe --topic myTopic --bootstrap-server host.docker.internal:9092
```

Output: 

```sh
Topic: myTopic  PartitionCount: 1       ReplicationFactor: 1    Configs:
        Topic: myTopic  Partition: 0    Leader: 1       Replicas: 1     Isr: 1
```

### Clean up

Shut down Docker Compose

```sh
$ docker-compose down
```
