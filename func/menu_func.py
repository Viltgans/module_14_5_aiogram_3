# Импорт необходимых модулей
from contextlib import suppress
from aiogram.exceptions import TelegramBadRequest
from aiogram.types import Message

# Импорт листов из файла handlers/Messages.py и handlers/Calculator.py
from ..handlers import Messages, Calculator


# Функция для удаления сообщений предшествующих меню
async def delete_pre_menu_messages(message: Message):
    with suppress(TelegramBadRequest):
        for msg_id in Messages.pre_menu_messages:
            await message.bot.delete_message(chat_id=message.chat.id, message_id=msg_id)
        Messages.pre_menu_messages.clear()


# Функция для удаления приветственного сообщения
async def delete_welcome_messages(message: Message):
    with suppress(TelegramBadRequest):
        for msg_id in Messages.welcome_messages:
            await message.bot.delete_message(chat_id=message.chat.id, message_id=msg_id)
        Messages.welcome_messages.clear()


# Функция для удаления сообщений меню 'Информация'
async def delete_menu_information(message: Message):
    with suppress(TelegramBadRequest):
        for msg_id in Messages.menu_info:
            await message.bot.delete_message(chat_id=message.chat.id, message_id=msg_id)
        Messages.menu_info.clear()


# Функция для удаления сообщений меню 'Рассчитать'
async def delete_menu_calc_and_formula(message: Message):
    with suppress(TelegramBadRequest):
        for msg_id in Messages.menu_messages:
            await message.bot.delete_message(chat_id=message.chat.id, message_id=msg_id)
        Messages.menu_messages.clear()


# Функция для удаления сообщений меню 'Регистрация'
async def delete_menu_registration(message: Message):
    with suppress(TelegramBadRequest):
        for msg_id in Messages.menu_registr:
            await message.bot.delete_message(chat_id=message.chat.id, message_id=msg_id)
        Messages.menu_registr.clear()


# Функция для удаления сообщений меню 'Купить'
async def delete_menu_buy(message: Message):
    with suppress(TelegramBadRequest):
        for msg_id in Messages.menu_buy:
            await message.bot.delete_message(chat_id=message.chat.id, message_id=msg_id)
        Messages.menu_buy.clear()


# Функция для удаления сообщений подменю 'Рассчитать' в обратном порядке
async def delete_all_menu_messages(message: Message):
    with suppress(TelegramBadRequest):
        chat_id = message.chat.id

        for msg_id in Calculator.formulas[::-1]:
            try:
                await message.bot.delete_message(chat_id=chat_id, message_id=msg_id)
            except Exception as e:
                print(f"Ошибка: {e}")
        Calculator.formulas.clear()

        for msg_id in Calculator.calories[::-1]:
            try:
                await message.bot.delete_message(chat_id=chat_id, message_id=msg_id)
            except Exception as e:
                print(f"Ошибка: {e}")
        Calculator.calories.clear()

        for msg_id in Calculator.messages_man[::-1]:
            try:
                await message.bot.delete_message(chat_id=chat_id, message_id=msg_id)
            except Exception as e:
                print(f"Ошибка: {e}")
        Calculator.messages_man.clear()

        for msg_id in Calculator.messages_woman[::-1]:
            try:
                await message.bot.delete_message(chat_id=chat_id, message_id=msg_id)
            except Exception as e:
                print(f"Ошибка: {e}")
        Calculator.messages_woman.clear()

        for msg_id in Calculator.messages[::-1]:
            try:
                await message.bot.delete_message(chat_id=chat_id, message_id=msg_id)
            except Exception as e:
                print(f"Ошибка: {e}")
        Calculator.messages.clear()

        for msg_id in Calculator.results[::-1]:
            try:
                await message.bot.delete_message(chat_id=chat_id, message_id=msg_id)
            except Exception as e:
                print(f"Ошибка: {e}")
        Calculator.results.clear()
