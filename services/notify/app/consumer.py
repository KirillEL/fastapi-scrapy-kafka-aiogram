from aiokafka import AIOKafkaConsumer
from loguru import logger

from bot import BOT
from infrastructure import config
import json


async def consume() -> None:
    consumer = AIOKafkaConsumer(
        config.CONSUME_TOPIC,
        bootstrap_servers=config.KAFKA_BOOTSTRAP_SERVERS
    )
    await consumer.start()
    try:
        async for msg in consumer:
            logger.info(f"Received message from currency service: {msg.value}")
            serialized = json.loads(msg.value)
            await BOT.send_message(
                chat_id=serialized.get("telegram_id"),
                text=serialized.get("currency_value") or "Валюта не найдена"
            )
    finally:
        await consumer.stop()
