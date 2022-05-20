from aiogram import types
from VK_API.vk_controller import *


async def send_welcome(message: types.Message):
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")


async def echo(message: types.Message):
    await message.answer(message.text)


async def take_last_post(message: types.Message):
    vk_group = 'mudakoff'
    vk_api_response = take_new_post(vk_group)
    await message.answer(vk_api_response)
