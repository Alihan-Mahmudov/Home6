import logging
from aiogram import executor
from config import dp
from hendlers import napominalka, fsm_anketa
from database.bot_base import sql_create
import asyncio

fsm_anketa.register_handlers_fsm_anketa(dp)
napominalka.register_handlers_napominalka(dp)

async def on_startup(_):
    asyncio.create_task(napominalka.scheduler())
    sql_create()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
    logging.basicConfig(level=logging.INFO )