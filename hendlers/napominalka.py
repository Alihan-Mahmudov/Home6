import aioschedule
from aiogram import types, Dispatcher
from config import bot
import asyncio

async def get_chat_id(mesage: types.Message):
    global chat_id
    chat_id = mesage.from_user.id
    await mesage.answer('OK')

async def vstavai():
    bot.send_message(chat_id=chat_id, text=" Забери игру в Epic games!!")

async def scheduler():
    aioschedule.every().day.at("22:00").do(vstavai)

    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(2)


def register_handlers_napominalka(dp: Dispatcher):
    dp.register_message_handler(get_chat_id,
                                lambda word: 'напомни' in word.text)