from aiogram import Bot, Dispatcher
from Telegram.Comands import *
import token_config


bot = Bot(token=token_config.t)

async def tbot_controller():
    try:
        disp = Dispatcher(bot=bot)
        disp.register_message_handler(start_handler, commands={"start", "restart"})
        await disp.start_polling()
    finally:
        await bot.close()