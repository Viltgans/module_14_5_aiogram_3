from aiogram import F, Router
from aiogram.types import CallbackQuery, Message, FSInputFile

from module_14.homework_14_5_v2.interface.text import *
from module_14.homework_14_5_v2.interface.button import *
from module_14.homework_14_5_v2.database.data_product import *
from module_14.homework_14_5_v2.database.data_user import *

router = Router()

initiate_product_db()
initiate_user_db()
products = get_all_products()

@router.message(F.text == "Купить")
async def get_buying_list(message: Message):
    for product in products:
        id_, title, description, price = product
        await message.answer(f'Название: {title} | Описание: {description} | Цена: {price}')
        photo = FSInputFile(f'files/Product{id_}.png', 'rb')
        await message.answer_photo(photo)
    await  message.answer(choose_product, reply_markup=buy_menu)

@router.callback_query(F.data == 'product_buying')
async def send_confirm_message(callback: CallbackQuery):
    await callback.message.answer(success_buy)
    await callback.answer()