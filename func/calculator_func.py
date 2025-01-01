# Импорт необходимых модулей
from contextlib import suppress
from aiogram.exceptions import TelegramBadRequest
from aiogram.types import Message, CallbackQuery

# Импорт листов из файла handlers/Calculator.py
from ..handlers import Calculator


# Функция для удаления сообщений в меню 'Рассчитать' при аргументе Message
async def delete_all_menu_calc_and_formula(message: Message):
    with suppress(TelegramBadRequest):
        chat_id = message.chat.id

        for msg_id in Calculator.messages:
            try:
                await message.bot.delete_message(chat_id=chat_id, message_id=msg_id)
            except Exception as e:
                print(f"Ошибка: {e}")
        Calculator.messages.clear()


# Функция для удаления сообщений в подменю 'Рассчитать' при аргументе Message
async def delete_submenu_calc_and_formula(message: Message):
    with suppress(TelegramBadRequest):
        chat_id = message.chat.id

        for msg_id in Calculator.formulas:
            try:
                await message.bot.delete_message(chat_id=chat_id, message_id=msg_id)
            except Exception as e:
                print(f"Ошибка: {e}")
        Calculator.formulas.clear()

        for msg_id in Calculator.messages_man:
            try:
                await message.bot.delete_message(chat_id=chat_id, message_id=msg_id)
            except Exception as e:
                print(f"Ошибка: {e}")
        Calculator.calories.clear()

        for msg_id in Calculator.messages_woman:
            try:
                await message.bot.delete_message(chat_id=chat_id, message_id=msg_id)
            except Exception as e:
                print(f"Ошибка: {e}")
        Calculator.messages_woman.clear()


# Функция для удаления сообщений в меню 'Рассчитать'
# подменю inline-кнопки 'Рассчитать норму калорий' при расчете нормы калорий
# для вывода полученной информации от пользователя при аргументе CallbackQuery
async def delete_messages_callback(callback: CallbackQuery):
    with suppress(TelegramBadRequest):
        for msg_id in Calculator.messages_input:
            try:
                await callback.bot.delete_message(chat_id=callback.message.chat.id, message_id=msg_id)
            except Exception as e:
                print(f"Ошибка: {e}")
        Calculator.messages_input.clear()


# Функция для удаления сообщений в меню 'Рассчитать'
# подменю inline-кнопки 'Рассчитать норму калорий' при расчете нормы калорий
# для мужчин при аргументе CallbackQuery
async def delete_man_messages(callback: CallbackQuery):
    with suppress(TelegramBadRequest):
        for msg_id in Calculator.messages_man:
            try:
                await callback.bot.delete_message(chat_id=callback.message.chat.id, message_id=msg_id)
            except Exception as e:
                print(f"Ошибка: {e}")
        Calculator.messages_man.clear()


# Функция для удаления сообщений в меню 'Рассчитать'
# подменю inline-кнопки 'Рассчитать норму калорий' при расчете нормы калорий
# для женщин при аргументе CallbackQuery
async def delete_woman_messages(callback: CallbackQuery):
    with suppress(TelegramBadRequest):
        for msg_id in Calculator.messages_woman:
            try:
                await callback.bot.delete_message(chat_id=callback.message.chat.id, message_id=msg_id)
            except Exception as e:
                print(f"Ошибка: {e}")
        Calculator.messages_woman.clear()


# Функция для удаления сообщений результатов в меню 'Рассчитать'
# подменю inline-кнопки 'Рассчитать норму калорий' при расчете нормы калорий
# при аргументе CallbackQuery
async def delete_result_messages(callback: CallbackQuery):
    with suppress(TelegramBadRequest):
        for msg_id in Calculator.results:
            try:
                await callback.bot.delete_message(chat_id=callback.message.chat.id, message_id=msg_id)
            except Exception as e:
                print(f"Ошибка: {e}")
        Calculator.results.clear()


# Функция для удаления сообщений в меню 'Рассчитать'
# подменю inline-кнопки 'Формулы расчёта' при аргументе CallbackQuery
async def delete_formulas(callback: CallbackQuery):
    with suppress(TelegramBadRequest):
        for msg_id in Calculator.formulas:
            try:
                await callback.bot.delete_message(chat_id=callback.message.chat.id, message_id=msg_id)
            except Exception as e:
                print(f"Ошибка: {e}")
        Calculator.formulas.clear()


# Функция для удаления сообщений результатов в меню 'Рассчитать'
# подменю inline-кнопки 'Рассчитать норму калорий'
async def delete_calories(callback: CallbackQuery):
    with suppress(TelegramBadRequest):
        for msg_id in Calculator.calories:
            try:
                await callback.bot.delete_message(chat_id=callback.message.chat.id, message_id=msg_id)
            except Exception as e:
                print(f"Ошибка: {e}")
        Calculator.calories.clear()
