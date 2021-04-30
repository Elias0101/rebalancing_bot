from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

to_roboadvisor = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Перейти к робоэдвайзеру")
        ]
    ],
    resize_keyboard=True
)

yes_markup = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Да")
        ]
    ],
    resize_keyboard=True
)
