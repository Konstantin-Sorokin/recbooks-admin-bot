def format_book_data(book_data: dict) -> str:

    return (
        f"📚 Название: {book_data.get('title', '❌о')}\n\n"
        f"📅 Год: {book_data.get('year', '❌')}\n\n"
        f"📝 Описание: {book_data.get('description', '❌')}\n\n"
        f"👤 Автор: {book_data.get('author', '❌')}\n\n"
        f"🏷️ Жанр: {book_data.get('genre', '❌')}"
    )
