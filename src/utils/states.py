from aiogram.fsm.state import StatesGroup, State


class BookState(StatesGroup):
    TITLE = State()
    AUTHOR = State()
    GENRE = State()
    DESCRIPTION = State()
    YEAR = State()


class AuthorState(StatesGroup):
    NAME = State()
    CONTENT = State()
    DATES = State()  # Годы жизни
    NATIONALITY = State()
