from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message

from module_14.homework_14_5_v2.interface.text import *
from module_14.homework_14_5_v2.interface.button import *

router = Router()

@router.message(Command('start'))
async def start(message: Message):
    await message.answer(hello, reply_markup = kb)

@router.message(F.text == "Рассчитать")
async def sing_up(message: Message):
    await message.answer(optional, reply_markup = inline_kb)

@router.message(F.text)
async def all_massages(message: Message):
    await message.answer('Введите команду /start, чтобы начать общение.')
