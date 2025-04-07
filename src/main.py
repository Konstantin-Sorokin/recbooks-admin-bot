import asyncio
import logging

from aiogram import Bot, Dispatcher

from utils.config import settings
from handlers import router


async def main():
    dp = Dispatcher()
    dp.include_router(router)
    logging.basicConfig(level=logging.INFO)
    bot = Bot(
        token=settings.bot.token,
    )
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
