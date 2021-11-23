from photo_url import unsplash

from aiogram import Bot, types
from aiogram.utils import executor
from aiogram.dispatcher import Dispatcher
import os


token = os.environ['token']
bot = Bot(token=token)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def process_start_command(message: types.Message):
    await bot.send_message(message.from_user.id, "Напиши, какую картинку ты ищешь")


@dp.message_handler()
async def echo_message(message: types.Message):
    photo_url = await unsplash.get_photo(message.text)
    if photo_url is None:
        await bot.send_message(message.from_user.id, "Фото по данному запросу не найдено(((")
    else:
        await bot.send_photo(message.from_user.id, photo_url)


if __name__ == '__main__':
    executor.start_polling(dp)

