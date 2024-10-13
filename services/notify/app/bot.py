from aiogram import Bot, Dispatcher, types
from infrastructure import config

dispatcher: Dispatcher = Dispatcher()
BOT = Bot(token=config.BOT_TOKEN)
