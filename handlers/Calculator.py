# Импорт необходимых модулей
from contextlib import suppress
from aiogram import html, Router, F
from aiogram.exceptions import TelegramBadRequest
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
# Импорт модулей с функциями из папки func, чтобы избавиться от дублирования кода
from ..func import repeat_calc
# Импорт клавиатуры с кнопками из файла interface/button.py
from ..interface.button import gender_kb, formulas_kb
# Импорт нужного текста из файла interface/text.py
from ..interface.text import *
# Импорт функций из файла func/calculator_func.py
from ..func import calculator_func

messages = []
messages_man = []
messages_woman = []
messages_input = []
formulas = []
calories = []
results = []

# Инициализация роутера
router = Router()


# Инициализация машины состояний для пользователя
class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()
    gender = State()


# Функция для inline-кнопки 'Формулы расчёта'
@router.callback_query(F.data == 'formulas')
async def get_formulas(callback: CallbackQuery):
    with suppress(TelegramBadRequest):
        # Инициализация
        bot_message = await callback.message.answer(gender_input, reply_markup=formulas_kb)
        formulas.append(bot_message.message_id)
        # Логика удаления сообщений
        if len(calories) > 0:
            await calculator_func.delete_calories(callback)
        if len(messages_woman) > 0:
            await calculator_func.delete_woman_messages(callback)
        if len(messages_man) > 0:
            await calculator_func.delete_man_messages(callback)
        if len(results) > 0:
            await calculator_func.delete_result_messages(callback)
        await callback.answer()


# Функция для inline-кнопки 'Рассчитать норму калорий'
@router.callback_query(F.data == 'calories')
async def set_gender(callback: CallbackQuery, state: FSMContext):
    with suppress(TelegramBadRequest):
        # Инициализация
        await state.set_state(UserState.gender)
        bot_message = await callback.message.answer(gender_input, reply_markup=gender_kb)
        calories.append(bot_message.message_id)
        # Логика удаления сообщений
        if len(formulas) > 0:
            await calculator_func.delete_formulas(callback)
        if len(messages_woman) > 0:
            await calculator_func.delete_woman_messages(callback)
        if len(messages_man) > 0:
            await calculator_func.delete_man_messages(callback)
        await callback.answer()


# Функция в подменю inline-кнопки 'Формулы расчёта' для inline-кнопки 'Мужской'
@router.callback_query(F.data == 'for_man')
async def get_formulas(callback: CallbackQuery):
    with suppress(TelegramBadRequest):
        # Инициализация
        bot_message = await callback.message.answer(formula_for_man)
        messages_man.append(bot_message.message_id)
        # Логика удаления сообщений
        if len(messages_woman) > 0:
            await calculator_func.delete_woman_messages(callback)
        await callback.answer()


# Функция в подменю inline-кнопки 'Формулы расчёта' для inline-кнопки 'Женский'
@router.callback_query(F.data == 'for_woman')
async def get_formulas(callback: CallbackQuery):
    with suppress(TelegramBadRequest):
        # Инициализация
        bot_message = await callback.message.answer(formula_for_woman)
        messages_woman.append(bot_message.message_id)
        # Логика удаления сообщений
        if len(messages_man) > 0:
            await calculator_func.delete_man_messages(callback)
        await callback.answer()


# Функция в подменю inline-кнопки 'Рассчитать норму калорий' для inline-кнопки 'Мужской'
@router.callback_query(F.data == 'man')
async def calc_for_man(callback: CallbackQuery, state: FSMContext):
    with suppress(TelegramBadRequest):
        # Инициализация
        await set_age(callback, state)
        # Логика удаления сообщений
        if len(results) > 0:
            await calculator_func.delete_result_messages(callback)
        if len(messages_woman) > 0:
            await calculator_func.delete_woman_messages(callback)
        await callback.answer()


# Функция в подменю inline-кнопки 'Рассчитать норму калорий' для inline-кнопки 'Женский'
@router.callback_query(F.data == 'woman')
async def calc_for_woman(callback: CallbackQuery, state: FSMContext):
    with suppress(TelegramBadRequest):
        # Инициализация
        await set_age(callback, state)
        # Логика удаления сообщений
        if len(results) > 0:
            await calculator_func.delete_result_messages(callback)
        if len(messages_man) > 0:
            await calculator_func.delete_man_messages(callback)
        await callback.answer()


# Функция расчета нормы калорий в подменю inline-кнопки 'Рассчитать норму калорий'
# Получение значения пола
@router.callback_query(UserState.gender)
async def set_age(callback: CallbackQuery, state: FSMContext):
    with suppress(TelegramBadRequest):
        # Инициализация
        await state.update_data(gender=callback.data)
        await state.set_state(UserState.age)
        data = await state.get_data()
        #  для inline-кнопки 'Мужской'
        if data['gender'] == 'man':
            bot_message = await callback.message.answer(man_age_input)
            # добавляем в список сообщений для удаления при аргументе Message
            messages.append(bot_message.message_id)
            # добавляем в список сообщений для удаления при аргументе CallbackQuery
            messages_man.append(bot_message.message_id)
        #  для inline-кнопки 'Женский'
        elif data['gender'] == 'woman':
            bot_message = await callback.message.answer(woman_age_input)
            # добавляем в список сообщений для удаления при аргументе Message
            messages.append(bot_message.message_id)
            # добавляем в список сообщений для удаления при аргументе CallbackQuery
            messages_woman.append(bot_message.message_id)
        await callback.answer()


# Функция расчета нормы калорий в подменю inline-кнопки 'Рассчитать норму калорий'
# Получение значения возраста
@router.message(UserState.age)
async def set_growth(message: Message, state: FSMContext):
    with suppress(TelegramBadRequest):
        user_message = message.text
        try:
            # Инициализация
            await state.update_data(age=int(user_message))
            # Удаление сообщения от пользователя
            await message.delete()
            # Вывод сообщения о введенных данных
            bot_message = await message.answer(f'<b>Введенный возраст: {user_message}</b>')
            # добавляем в список сообщений для удаления при аргументе Message
            messages.append(bot_message.message_id)
            # добавляем в список сообщений для удаления при аргументе CallbackQuery
            messages_input.append(bot_message.message_id)
            await state.set_state(UserState.growth)
            data = await state.get_data()
            #  для inline-кнопки 'Мужской'
            if data['gender'] == 'man':
                bot_message = await message.answer(man_growth_input)
                # добавляем в список сообщений для удаления при аргументе Message
                messages.append(bot_message.message_id)
                # добавляем в список сообщений для удаления при аргументе CallbackQuery
                messages_man.append(bot_message.message_id)
            #  для inline-кнопки 'Женский'
            elif data['gender'] == 'woman':
                bot_message = await message.answer(woman_growth_input)
                # добавляем в список сообщений для удаления при аргументе Message
                messages.append(bot_message.message_id)
                # добавляем в список сообщений для удаления при аргументе CallbackQuery
                messages_woman.append(bot_message.message_id)
        # Обработка ошибок ввода данных и других reply-кнопок основного меню
        except ValueError:
            # Если в процессе расчета пользователь выбрал кнопку 'Информация', вывод меню кнопки 'Информация'
            if message.text == 'Информация':
                await repeat_calc.repeat_calc_info(message, state)
            # Если в процессе расчета пользователь выбрал кнопку 'Регистрация', вывод меню кнопки 'Информация'
            if message.text == 'Регистрация':
                await repeat_calc.repeat_calc_reg(message, state)
            # Если в процессе расчета пользователь выбрал кнопку 'Купить', вывод меню кнопки 'Информация'
            if message.text == 'Купить':
                await repeat_calc.repeat_calc_buy(message, state)
            else:
                # Удаление сообщения от пользователя с ошибкой ввода данных
                await message.delete()
                # Вывод сообщения об ошибке ввода данных
                bot_message = await message.answer(age_error)
                messages.append(bot_message.message_id)


# Функция расчета нормы калорий в подменю inline-кнопки 'Рассчитать норму калорий'
# Получение значения роста
@router.message(UserState.growth)
async def set_weight(message: Message, state: FSMContext):
    with suppress(TelegramBadRequest):
        try:
            # Инициализация
            user_message = message.text
            await state.update_data(growth=int(user_message))
            # Удаление сообщения от пользователя
            await message.delete()
            # Вывод сообщения о введенных данных
            bot_message = await message.answer(f'<b>Введенный рост: {user_message}</b>')
            # добавляем в список сообщений для удаления при аргументе Message
            messages.append(bot_message.message_id)
            # добавляем в список сообщений для удаления при аргументе CallbackQuery
            messages_input.append(bot_message.message_id)
            await state.set_state(UserState.weight)
            data = await state.get_data()
            #  для inline-кнопки 'Мужской'
            if data['gender'] == 'man':
                bot_message = await message.answer(man_weight_input)
                # добавляем в список сообщений для удаления при аргументе Message
                messages.append(bot_message.message_id)
                # добавляем в список сообщений для удаления при аргументе CallbackQuery
                messages_man.append(bot_message.message_id)
            #  для inline-кнопки 'Женский'
            elif data['gender'] == 'woman':
                bot_message = await message.answer(woman_weight_input)
                # добавляем в список сообщений для удаления при аргументе Message
                messages.append(bot_message.message_id)
                # добавляем в список сообщений для удаления при аргументе CallbackQuery
                messages_woman.append(bot_message.message_id)
        # Обработка ошибок ввода данных и других reply-кнопок основного меню
        except ValueError:
            # Если в процессе расчета пользователь выбрал кнопку 'Информация', вывод меню кнопки 'Информация'
            if message.text == 'Информация':
                await repeat_calc.repeat_calc_info(message, state)
            # Если в процессе расчета пользователь выбрал кнопку 'Регистрация', вывод меню кнопки 'Информация'
            if message.text == 'Регистрация':
                await repeat_calc.repeat_calc_reg(message, state)
            # Если в процессе расчета пользователь выбрал кнопку 'Купить', вывод меню кнопки 'Информация'
            if message.text == 'Купить':
                await repeat_calc.repeat_calc_buy(message, state)
            else:
                # Удаление сообщения от пользователя с ошибкой ввода данных
                await message.delete()
                # Вывод сообщения об ошибке ввода данных
                bot_message = await message.answer(growth_error)
                messages.append(bot_message.message_id)


# Функция расчета нормы калорий в подменю inline-кнопки 'Рассчитать норму калорий'
# Получение значения веса
@router.message(UserState.weight)
async def send_calories(message: Message, state: FSMContext):
    with suppress(TelegramBadRequest):
        try:
            user_message = message.text
            await state.update_data(weight=int(user_message))
            # Удаление сообщения от пользователя
            await message.delete()
            # Вывод сообщения о введенных данных
            bot_message = await message.answer(f'<b>Введенный вес: {user_message}</b>')
            # добавляем в список сообщений для удаления при аргументе Message
            messages.append(bot_message.message_id)
            # добавляем в список сообщений для удаления при аргументе CallbackQuery
            messages_input.append(bot_message.message_id)
            data = await state.get_data()
            #  для inline-кнопки 'Мужской'
            if data['gender'] == 'man':
                # Удаляем все сообщения при расчете нормы калорий
                await calculator_func.delete_all_menu_calc_and_formula(message)
                # Расчет нормы калорий
                result = (10 * int(data['weight']) + 6.25 * int(data['growth']) - 5 * int(data['age']) + 5)
                # Вывод сообщения о результате расчета
                bot_message = await message.answer(f'{html.bold(html.quote(message.from_user.full_name))}! '
                                                   f'Ваша норма калорий <b>{result:.2f}</b>', parse_mode='HTML')
                results.append(bot_message.message_id)
            #  для inline-кнопки 'Женский'
            elif data['gender'] == 'woman':
                # Удаляем все сообщения при расчете нормы калорий
                await calculator_func.delete_all_menu_calc_and_formula(message)
                # Расчет нормы калорий
                result = (10 * int(data['weight']) + 6.25 * int(data['growth']) - 5 * int(data['age']) - 161)
                # Вывод сообщения о результате расчета
                bot_message = await message.answer(f'{html.bold(html.quote(message.from_user.full_name))}! '
                                                   f'Ваша норма калорий <b>{result:.2f}</b>', parse_mode='HTML')
                results.append(bot_message.message_id)
            # Очистка данных машины состояний
            await state.clear()
        except ValueError:
            # Если в процессе расчета пользователь выбрал кнопку 'Информация', вывод меню кнопки 'Информация'
            if message.text == 'Информация':
                await repeat_calc.repeat_calc_info(message, state)
            # Если в процессе расчета пользователь выбрал кнопку 'Регистрация', вывод меню кнопки 'Информация'
            if message.text == 'Регистрация':
                await repeat_calc.repeat_calc_reg(message, state)
            # Если в процессе расчета пользователь выбрал кнопку 'Купить', вывод меню кнопки 'Информация'
            if message.text == 'Купить':
                await repeat_calc.repeat_calc_buy(message, state)
            else:
                # Удаление сообщения от пользователя с ошибкой ввода данных
                await message.delete()
                # Вывод сообщения об ошибке ввода данных
                bot_message = await message.answer(weight_error)
                messages.append(bot_message.message_id)
