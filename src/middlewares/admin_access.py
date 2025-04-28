from aiogram import BaseMiddleware
from aiogram.types import TelegramObject, User


class AdminAccessMiddleware(BaseMiddleware):
    def __init__(self, admin_ids: list[int]):
        self.admin_ids = admin_ids

    async def __call__(self, handler, event: TelegramObject, data: dict):
        user: User = data.get("event_from_user")
        if user is not None and user.id in self.admin_ids:
            return await handler(event, data)
        return
