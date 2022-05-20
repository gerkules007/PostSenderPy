from aiogram import Bot, Dispatcher, executor
from Telegram.tbot_comands_handler import *
import token_config


def tbot_controller():
    bot = Bot(token=token_config.telegram)
    dp: Dispatcher = Dispatcher(bot=bot)

    dp.register_message_handler(send_welcome, commands={"start", "restart"})
    dp.register_message_handler(take_last_post, commands={"take_last_post"})

    executor.start_polling(dp, skip_updates=True)

