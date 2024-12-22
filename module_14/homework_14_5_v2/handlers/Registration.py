from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from module_14.homework_14_5_v2.interface.text import *
from aiogram.fsm.state import State, StatesGroup
from module_14.homework_14_5_v2.database.data_user import *


router = Router()

class RegistrationState(StatesGroup):
    username = State()
    email = State()
    age = State()

@router.message(F.text == "Регистрация")
async def main_menu(message: Message, state: FSMContext):
    await message.answer(name_input)
    await state.set_state(RegistrationState.username)

@router.message(RegistrationState.username)
async def set_username(message: Message, state: FSMContext):
    username = message.text
    if is_included(username):
        await message.answer(user_exist)
        return

    await state.update_data(username=message.text)
    await message.answer(email_input)
    await state.set_state(RegistrationState.email)

@router.message(RegistrationState.email)
async def set_email(message: Message, state: FSMContext):
    await state.update_data(email=message.text)
    await message.answer(age_input)
    await state.set_state(RegistrationState.age)

@router.message(RegistrationState.age)
async def set_age_reg(message: Message, state: FSMContext):
    await state.update_data(age = message.text)
    data = await state.get_data()
    add_user(data['username'], data['email'], data['age'])
    await message.answer(success_reg)
    await state.clear()