from aiogram.dispatcher.filters import Command
from aiogram import types
from aiogram.types import CallbackQuery

from keyboards.inline.callback_datas import product_callback
from keyboards.inline.edit_markup import edit_markup
from keyboards.inline.product_markup import create_edit_markup
from loader import dp


@dp.message_handler(Command("inline_buttons_1"))
async def introduction(message: types.Message):
    await message.answer("Edit @Sberleadbot info.\n\n"
                         "Name: Бот для Заданий на Курсе Udemy\n"
                         "Description: ?\n"
                         "About: ?\n"
                         "Botpic: ? no botpic\n"
                         "Commands: no commands yet\n",
                         reply_markup=edit_markup)


@dp.message_handler(Command("items"))
async def show_items(message: types.Message):
    await message.answer_photo(photo="https://legkovmeste.ru/wp-content/uploads/2019/03/post_5c8b918b63def.jpg",
                               caption="papaya", reply_markup=create_edit_markup("papaya", 1))
    await message.answer_photo(
        photo="https://cdn.lifehacker.ru/wp-content/uploads/2015/02/Depositphotos_12802788_m.jpg",
        caption="avocado", reply_markup=create_edit_markup("avocado", 2))


@dp.callback_query_handler(product_callback.filter(action="buy"))
async def buying_product(call: CallbackQuery, callback_data: dict):
    product_id = callback_data.get("id")
    await call.message.edit_caption(f"Покупай товар номер {product_id}!")
    await call.message.edit_reply_markup()


@dp.callback_query_handler(product_callback.filter(action="like"))
async def like_product(call: CallbackQuery, callback_data: dict):
    await call.answer("Тебе понравился этот товар", show_alert=False)


@dp.callback_query_handler(product_callback.filter(action="deslike"))
async def like_product(call: CallbackQuery, callback_data: dict):
    await call.answer("Тебе не понравился этот товар", show_alert=False)

