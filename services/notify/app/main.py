import asyncio
import json
from bot import BOT, dispatcher
import consumer
from loguru import logger


async def main() -> None:
    polling = asyncio.create_task(dispatcher.start_polling(BOT))
    consuming = asyncio.create_task(consumer.consume())
    await asyncio.gather(polling, consuming)
    logger.info("Started polling bot!")


if __name__ == "__main__":
    asyncio.run(main())
