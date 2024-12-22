# 🏦 Transaction Simulator

![License](https://img.shields.io/github/license/avcaliani/tx-simulator?logo=apache&color=lightseagreen)
![#](https://img.shields.io/badge/python-3.13.x-blue.svg?logo=python&logoColor=white)
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
```

Then, execute the Python script.

```bash
# Activate the VEnv 👇
source .venv/bin/activate

# Run the script 👇
python main.py
```

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
