from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode

from .config import Config, load_config

config: Config = load_config(".env")
bot: Bot = Bot(token=config.tg_bot.BOT_TOKEN, parse_mode=ParseMode.HTML)
dp: Dispatcher = Dispatcher()
