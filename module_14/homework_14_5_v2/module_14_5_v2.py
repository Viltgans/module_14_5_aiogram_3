from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
import asyncio

from module_14.homework_14_5_v2.handlers import Messages, Registration, Buying, Calculator


async def main():
    api = '7913615067:AAEeXF1fJTlHswTcBZkUZydPjQ_sXYOUK1Y'
    bot = Bot(token = api)
    dp = Dispatcher(storage = MemoryStorage())

    dp.include_routers(Calculator.router)
    dp.include_routers(Buying.router)
    dp.include_routers(Registration.router)
    dp.include_routers(Messages.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())