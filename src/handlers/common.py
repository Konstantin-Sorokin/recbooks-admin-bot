from aiogram.fsm.context import FSMContext


async def set_default_book_data(state: FSMContext) -> dict[str, str]:
    book_data = {
        "title": "❌",
        "year": "❌",
        "description": "❌",
        "author": "❌",
        "genre": "❌",
    }
    await state.update_data(book_data=book_data)
    return book_data
