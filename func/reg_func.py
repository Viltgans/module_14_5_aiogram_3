# Импорт необходимых модулей
from contextlib import suppress
from aiogram.exceptions import TelegramBadRequest
from aiogram.types import Message

# Импорт листов из файла handlers/Registration.py
from ..handlers import Registration


# Функция для удаления всех сообщений, которые были отправлены в чат
# во время инициализации кнопки меню "Регистрация" и самой регистрации.
async def delete_all_reg_menu_messages(message: Message):
    with suppress(TelegramBadRequest):
        chat_id = message.chat.id

        for msg_id in Registration.reg_messages[::-1]:
            try:
                await message.bot.delete_message(chat_id=chat_id, message_id=msg_id)
            except Exception as e:
                print(f"Ошибка: {e}")
        Registration.reg_messages.clear()

        for msg_id in Registration.user_info[::-1]:
            try:
                await message.bot.delete_message(chat_id=chat_id, message_id=msg_id)
            except Exception as e:
                print(f"Ошибка: {e}")
        Registration.user_info.clear()

        for msg_id in Registration.reg_results[::-1]:
            try:
                await message.bot.delete_message(chat_id=chat_id, message_id=msg_id)
            except Exception as e:
                print(f"Ошибка: {e}")
        Registration.reg_results.clear()
