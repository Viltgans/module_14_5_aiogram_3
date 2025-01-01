# Импорт необходимых модулей
from contextlib import suppress
from aiogram.exceptions import TelegramBadRequest
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
# Импорт листов из файла handlers/Messages.py
from ..handlers import Messages
# Импорт функций для работы с кнопками
from ..func import reg_func
# Импорт модуля с функцией для его запуска
from ..handlers.Buying import get_buying_list
# Импорт нужного текста из файла interface/text.py
from ..interface.text import *
# Импорт клавиатуры с кнопками из файла interface/button.py
from ..interface.button import inline_kb
# Импорт функций из файла func/menu_func.py
from ..func import menu_func


async def repeat_reg_info(message: Message, state: FSMContext):
    with suppress(TelegramBadRequest):
        # Удаление сообщения от пользователя с кнопкой 'Информация'
        await message.delete()
        # Очистка данных машины состояния
        await state.clear()
        # Удаление всех сообщений от кнопки 'Регистрация'
        await menu_func.delete_menu_registration(message)
        await reg_func.delete_all_reg_menu_messages(message)
        # Вывод меню кнопки 'Информация'
        info_message = await message.answer(information_text)
        Messages.menu_info.append(info_message.message_id)


async def repeat_reg_calc(message: Message, state: FSMContext):
    with suppress(TelegramBadRequest):
        # Удаление сообщения от пользователя с кнопкой 'Рассчитать'
        await message.delete()
        # Очистка данных машины состояния
        await state.clear()
        # Удаление всех сообщений от кнопки 'Регистрация'
        await reg_func.delete_all_reg_menu_messages(message)
        await menu_func.delete_menu_registration(message)
        # Вывод меню кнопки 'Рассчитать'
        menu_message = await message.answer(optional, reply_markup=inline_kb)
        Messages.menu_messages.append(menu_message.message_id)


async def repeat_reg_buy(message: Message, state: FSMContext):
    with suppress(TelegramBadRequest):
        # Удаление сообщения от пользователя с кнопкой 'Купить'
        await message.delete()
        # Очистка данных машины состояния
        await state.clear()
        # Удаление всех сообщений от кнопки 'Регистрация'
        await reg_func.delete_all_reg_menu_messages(message)
        await menu_func.delete_menu_registration(message)
        # Вывод меню кнопки 'Купить'
        await get_buying_list(message)
