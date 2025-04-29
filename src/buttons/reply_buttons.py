from dataclasses import dataclass

from aiogram.types import KeyboardButton


@dataclass
class ReplyButton:
    text: str

    @property
    def button(self) -> KeyboardButton:
        return KeyboardButton(text=self.text)


CREATE_AUTHOR = ReplyButton("Добавить автора 🥷")
EDIT_AUTHOR = ReplyButton("Редактировать автора 📝")
CREATE_BOOK = ReplyButton("Добавить книгу 📖")
EDIT_BOOK = ReplyButton("Редактировать книгу 📝")
