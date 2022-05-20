from aiogram import Bot, Dispatcher, executor
from Telegram.Comands import *
import token_config


bot = Bot(token=token_config.t)
dp: Dispatcher = Dispatcher(bot=bot)

dp.register_message_handler(send_welcome, commands={"start", "restart"})


def tbot_controller():
    executor.start_polling(dp, skip_updates=True)

