import json

from fastapi import Depends

from core.kafka.producer import get_producer, AIOWebProducer
from shared.schemas import MessageCreateDto
from .router import currency_router


@currency_router.post(
    "/send_info"
)
async def send_currency_info(message: MessageCreateDto, producer: AIOWebProducer = Depends(get_producer)) -> None:
    message = json.dumps(message.model_dump()).encode("utf-8")
    await producer.send(message)
