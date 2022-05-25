from aiogram import Bot, Dispatcher, executor
from Telegram.tbot_comands_handler import *
import json


with open('config\\tg_config.json', 'r', encoding='utf-8') as jtg:
    tg_cfg = json.load(jtg)

bot = Bot(token=tg_cfg['token'])
dp: Dispatcher = Dispatcher(bot=bot)


def tbot_controller():
    dp.register_message_handler(send_welcome, commands={"start", "restart"})
    dp.register_message_handler(take_last_post, commands={"take_last_post"})

    executor.start_polling(dp, skip_updates=True)

