from aiogram import types, executor, Dispatcher
from config import bot
from keyboards.client_kb import comands_markup
from parser.news import parser


async def start_hendler(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id, text='Привет!!')

async def comands_hendler(message: types.Message):
    if message.chat.type != 'privat':
        await message.answer("Пиши в личку!!")
    else:
        await bot.send_message(chat_id=message.from_user.id, reply_markup=comands_markup)

async def get_news(message: types.Message):
    news = parser()
    for i in news:
        await message.answer(
            f"{i['link']}\n"
            f"{i['title']}\n"
            f"{i['price']} грн"
        )

def register_comands_hendler(dp: Dispatcher):
      dp.register_message_handler(get_news, commands=['News'])
#     dp.register_message_handler(start_hendler, commands='start')
#
#     dp.register_message_handler(comands_markup, commands='command')
#     dp.register_message_handler(comands_markup,

