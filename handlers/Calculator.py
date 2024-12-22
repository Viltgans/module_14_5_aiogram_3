from aiogram import Router, F
from aiogram.types import Message, CallbackQuery

from module_14.homework_14_5_v2.interface.button import formulas_kb, gender_kb
from module_14.homework_14_5_v2.interface.text import *
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

router = Router()

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()
    gender = State()

@router.callback_query(F.data == 'formulas')
async def get_formulas(callback: CallbackQuery):
    await callback.message.answer(optional, reply_markup = formulas_kb)
    await callback.answer()

@router.callback_query(F.data == 'for_men')
async def get_formulas(callback: CallbackQuery):
    await callback.message.answer(formula_for_men)
    await callback.answer()

@router.callback_query(F.data == 'for_women')
async def get_formulas(callback: CallbackQuery):
    await callback.message.answer(formula_for_women)
    await callback.answer()

@router.callback_query(F.data == 'calories')
async def set_gender(callback: CallbackQuery, state: FSMContext):
    await state.set_state(UserState.gender)
    await callback.message.answer(gender_input, reply_markup = gender_kb)
    await callback.answer()

@router.callback_query(UserState.gender)
async def set_age(callback: CallbackQuery, state: FSMContext):
    await state.update_data(gender = callback.data)
    await state.set_state(UserState.age)
    await callback.message.answer(age_input)
    await callback.answer()

@router.message(UserState.age)
async def set_growth(message: Message, state: FSMContext):
    await state.update_data(age = message.text)
    await state.set_state(UserState.growth)
    await message.answer(growth_input)

@router.message(UserState.growth)
async def set_weight(message: Message, state: FSMContext):
    await state.update_data(growth = message.text)
    await state.set_state(UserState.weight)
    await message.answer(weight_input)

@router.message(UserState.weight)
async def send_calories(message: Message, state: FSMContext):
    await state.update_data(weight = message.text)
    data = await state.get_data()
    if data['gender'] == 'Мужской':
        result = (10 * int(data['weight']) + 6.25 * int(data['growth']) - 5 * int(data['age']) + 5)
    else:
        result = (10 * int(data['weight']) + 6.25 * int(data['growth']) - 5 * int(data['age']) - 161)
    await message.answer(f'Ваша норма калорий {result:.2f}')
    await state.clear()