import json
import random
import uuid
from argparse import ArgumentParser, Namespace
from datetime import UTC, datetime
from time import sleep
from typing import Any, Tuple

from kafka.errors import NoBrokersAvailable
from kafka.producer.future import FutureRecordMetadata, RecordMetadata

from kafka import KafkaProducer


def get_args() -> Namespace:
    parser = ArgumentParser(description="🏦 Transaction Simulator")
    parser.add_argument(
        "-s",
        type=str,
        dest="kafka_server",
        default="localhost:9092",
        help="Kafka server addresses, splitted by ',' (default: localhost:9092).",
    )
    parser.add_argument(
        "-t",
        type=str,
        dest="kafka_topic",
        default="NTH_TRANSACTIONS_V1",
        help="Kafka topic to publish the data (default: NTH_TRANSACTIONS_V1).",
    )
    parser.add_argument(
        "--sleep",
        type=float,
        default=0.25,
        help="The sleep duration between messages (default: 0.25).",
    )
    return parser.parse_args()


def new_transaction() -> Tuple[str, dict]:
    customer_id = f"c{random.randint(1, 1_000_000):09d}"
    is_suspect = random.choice([True, False])
    transaction = {
        "tx_id": str(uuid.uuid4()),
        "customer_id": customer_id,
        "terminal_id": f"t{random.randint(1, 22):03d}",
        "tx_datetime": datetime.now(UTC).strftime("%Y-%m-%d %H:%M:%S.%f"),
        "tx_amount": round(random.uniform(0.1, 1_000_000.0), 2),
        "tx_fraud_suspect": is_suspect,
        "tx_fraud_reason_id": random.randint(1, 10) if is_suspect else None,
    }
    return customer_id, transaction


def green(value: Any) -> str:
    return f"\033[1;32m{value}\033[00m"


def red(value: Any) -> str:
    return f"\033[1;31m{value}\033[00m"


def show_sent_message(response: FutureRecordMetadata) -> None:
    metadata: RecordMetadata = response.get()
    timestamp = datetime.fromtimestamp(metadata.timestamp / 1000, UTC)
    print(
        f"📦 "
        f"{green('T')}: {metadata.topic} | "
        f"{green('P')}: {metadata.partition} | "
        f"{green('O')}: {metadata.offset} | "
        f"{green('TS')}: {timestamp.strftime('%Y-%m-%d %H:%M:%S')}"
    )


def publish_to_kafka(server: str, topic: str, sleep_time: int):
    producer = KafkaProducer(
        bootstrap_servers=server.split(","),
        value_serializer=lambda v: json.dumps(v).encode("utf-8"),
    )
    try:
        while True:
            msg_key, msg_payload = new_transaction()
            response = producer.send(
                topic=topic, key=bytes(msg_key, "utf-8"), value=msg_payload
            )
            show_sent_message(response)
            sleep(sleep_time)
    finally:
        producer.close()


if __name__ == "__main__":
    args = get_args()
    print(green("🏦 Transaction Simulator"))
    print(args)
    try:
        publish_to_kafka(args.kafka_server, args.kafka_topic, args.sleep)
    except NoBrokersAvailable:
        print(f"{red('Error!')} No broker available, is your kafka up?")
    except KeyboardInterrupt:
        print("\nSee ya 👋")
