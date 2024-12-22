<img src="https://apache.org/logos/res/kafka/kafka_highres.png" width="128px" align="right"/>

# 📟 Kafka on CLI

You have to up your docker environment, then you will be able to use your own Kafka.

One thing you can do is to check the container logs, like this...

```bash
docker-compose logs kafka
```

## Docker Structure

```bash
kafka
├── Dockerfile        # 🐋 Main docker file.
├── README.md         # 😁 This document.
├── init.sh           # 🟢 Initialization script for ZooKeeper and Kafka.
└── kafka.properties  # 📝 Kafka properties with custom configs.
```

## Playground

Here are some terminal commands you can try to explore your own Kafka 😎

```bash
# Creating your first topic \o/
docker compose exec kafka kafka-topics.sh \
    --create \
    --bootstrap-server "localhost:9092" \
    --replication-factor "1" \
    --partitions "1" \
    --topic "MY_TOPIC"

# Checking the available topics
docker compose exec kafka kafka-topics.sh --list --bootstrap-server "localhost:9092"

# Producing messages ✉️
docker compose exec kafka kafka-console-producer.sh \
    --broker-list "localhost:9092" \
    --topic "MY_TOPIC"

# Consuming messages 🔎
docker compose exec kafka kafka-console-consumer.sh \
    --bootstrap-server "localhost:9092" \
    --topic "MY_TOPIC" --from-beginning

# Checking our topics
docker compose exec kafka kafka-consumer-groups.sh \
    --all-groups \
    --describe \
    --bootstrap-server "localhost:9092"
```

## Useful Links

- [Apache Kafka](https://kafka.apache.org/downloads)
- [Kafka Tool - UI Tool 4 Kafka](https://www.kafkatool.com/download.html)
- [Medium: Learning in Practice](https://medium.com/trainingcenter/apache-kafka-codifica%C3%A7%C3%A3o-na-pratica-9c6a4142a08f)
