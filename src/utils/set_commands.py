from aiogram.types import BotCommand, BotCommandScopeChat
from aiogram import Bot

from utils import constants, settings

admin_commands = [
    BotCommand(
        command=constants.START_COMMAND, description="Стартовая команда для админа"
    ),
    BotCommand(command=constants.CREATE_BOOK_COMMAND, description="Создать книгу"),
]


async def set_commands(bot: Bot):
    await bot.set_my_commands(
        admin_commands,
        scope=BotCommandScopeChat(chat_id=settings.bot.admins),
    )
