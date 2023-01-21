from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def main_menu():
    markup = InlineKeyboardMarkup()

    btn1 = InlineKeyboardButton("", callback_data='')
    btn1 = InlineKeyboardButton("", callback_data='')
    btn1 = InlineKeyboardButton("", callback_data='')

    markup.add(back_btn())
    return markup


def back_btn():
    back = InlineKeyboardButton("Назад", callback_data='back')

    return back
