# 🏦 Transaction Simulator

![License](https://img.shields.io/github/license/avcaliani/tx-simulator?logo=apache&color=lightseagreen)
![#](https://img.shields.io/badge/python-3.11.x-blue.svg?logo=python&logoColor=white)
![#](https://img.shields.io/badge/kafka-3.9.x-lightgray.svg?logo=apache-kafka&logoColor=white)

## What is this project?

**TL;DR;** There is a Python script that generate "fake" transaction data and publish to a Kafka Topic.

By many times I'm creating PoCs and I need some data,
so I always have to search or create some script to generate some data,
this what this repisitory for.

## How do I execute this project?

You just need to execute the services 🚀

```bash
# Up the Kafka nodes 👇
docker compose up -d

# Activate the VEnv 👇
source .venv/bin/activate

# Run the script 👇
python main.py

# In another terminal, you can check the messages...
docker compose exec kafka kafka-console-consumer.sh \
    --bootstrap-server "localhost:9092" \
    --topic "NTH_TRANSACTIONS_V1" --from-beginning
```

Here is a payload example.

```json
{
    "tx_id": "32686c3b-8d55-446c-8bd0-ab48f2694f5c",
    "customer_id": "c000269995",
    "terminal_id": "t001",
    "tx_datetime": "2024-12-22 13:42:48.847598",
    "tx_amount": 477.58,
    "tx_fraud_suspect": true,
    "tx_fraud_reason": 1
}
```

Other data files can be found in the [data](./data) folder.

To shutdown the services, you just need to execute...

```bash
docker compose down
```

### Don't have a VEnv?

```bash
# Optional Step 👇
pyenv local 3.13.1

# Creating Python virtual env 👇
python3 -m venv .venv \
    && source .venv/bin/activate \
    && pip install --upgrade pip

# Installing project dependencies 👇
pip install -r requirements.txt
```
