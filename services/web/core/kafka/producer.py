from aiokafka import AIOKafkaProducer
from infrastructure import config
import asyncio

event_loop = asyncio.get_event_loop()


class AIOWebProducer(object):
    def __init__(self):
        self.__producer: AIOKafkaProducer = AIOKafkaProducer(
            bootstrap_servers=config.KAFKA_BOOTSTRAP_SERVERS,
            loop=event_loop
        )
        self.__produce_topic = config.WEB_TOPIC

    async def start(self) -> None:
        await self.__producer.start()

    async def stop(self) -> None:
        if not self.__producer:
            raise RuntimeError('Producer not started')
        await self.__producer.stop()

    async def send(self, value: bytes) -> None:
        await self.start()
        try:
            await self.__producer.send(
                topic=self.__produce_topic,
                value=value
            )
        finally:
            await self.stop()


def get_producer() -> AIOWebProducer:
    return AIOWebProducer()
