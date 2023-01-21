from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from loader import dp

from message_texts import texts as t
from help_functions.sql import user as u
from keyboards.inline.mane_kb import main_menu



@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Привет, {message.from_user.full_name}!")
    user_id = message.from_user.id
    if not u.check_user(user_id):
        u_name = message.from_user.full_name
        await message.answer(t.hello_text)
        u.main_info_fill((user_id, u_name))
    await message.answer(t.menu_text, reply_markup=main_menu())


