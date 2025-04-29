from dataclasses import dataclass

from aiogram.types import InlineKeyboardButton


@dataclass
class InlineButton:
    text: str
    callback_data: str

    @property
    def button(self) -> InlineKeyboardButton:
        return InlineKeyboardButton(text=self.text, callback_data=self.callback_data)


CONFIRM = InlineButton(text="Подтвердить", callback_data="confirm")

BACK_TO_BOOK_DATA = InlineButton(text="Назад", callback_data="book_data")
BOOK_AUTHOR = InlineButton(text="Автор", callback_data="book_author")
BOOK_TITLE = InlineButton(text="Название", callback_data="book_title")
BOOK_YEAR = InlineButton(text="Год", callback_data="book_year")
BOOK_GENRE = InlineButton(text="Жанр", callback_data="book_genre")
BOOK_DESCRIPTION = InlineButton(text="Описание", callback_data="book_description")
BOOK_RESET = InlineButton(text="Сбросить", callback_data="reset_book")

AUTHOR_NAME = InlineButton(text="Имя", callback_data="author_name")
AUTHOR_DATES = InlineButton(text="Годы жизни", callback_data="author_dates")
AUTHOR_NATIONALITY = InlineButton(
    text="Национальность", callback_data="author_nationality"
)
AUTHOR_CONTENT = InlineButton(text="Биография", callback_data="author_content")
