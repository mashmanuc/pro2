import logging
import aiogram.utils.markdown as md
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.utils import executor
from dotenv import load_dotenv
import os
load_dotenv()

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)

# Включіть логування з використанням middleware
dp.middleware.setup(LoggingMiddleware())

# Обробник команди /start
@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    """
    Вітаємо користувача
    """
    await message.reply("Привіт, {0.first_name}! Я - {1.first_name}, бот для повторення тексту.".format(message.from_user, bot))

# Обробник усіх текстових повідомлень
@dp.message_handler()
async def echo(message: types.Message):
    """
    Повторення отриманого повідомлення назад
    """
    await message.answer(message.text)

if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)
