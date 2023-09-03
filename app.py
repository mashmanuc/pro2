from aiogram import Bot
import os
from dotenv import load_dotenv,find_dotenv
from aiogram import types,  Dispatcher
from aiogram.utils import executor
load_dotenv()
ad=os.getenv('AD')
bot = Bot(token=os.getenv('TOKEN'))
dp=Dispatcher(bot)
print('''Bottttttttttt''')


@dp.message_handler()
async def cancel_handler(message:types.Message):
    print(message.text)
    await message.reply(message.text)





if __name__=='__main__':
    executor.start_polling(dp)
