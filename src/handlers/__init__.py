from aiogram import Router

from handlers.callback import router as callbacks_router
from handlers.command import router as commands_router
from handlers.message import router as messages_router

router = Router()

router.include_routers(
    callbacks_router,
    commands_router,
    messages_router,
)

__all__ = ["router"]
