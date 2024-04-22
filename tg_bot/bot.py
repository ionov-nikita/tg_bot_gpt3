import asyncio
import logging

from common.create_bot import bot, dp
from src.handlers import router

logger = logging.getLogger(__name__)


async def run_bot() -> None:

    dp.include_router(router)

    logger.info("Bot is running")

    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(filename)s:%(lineno)d #%(levelname)-8s "
        "[%(asctime)s] - %(name)s - %(message)s",
    )

    try:
        asyncio.run(run_bot())
    except (KeyboardInterrupt, SystemExit):
        logger.info("Bot stopped")
