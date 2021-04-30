from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from loader import dp
from aiogram import types
from states import Test


@dp.message_handler(Command("form"))
async def enter_test(message: types.Message):
    await message.answer("What's your name?")
    await Test.Q1.set()


@dp.message_handler(state=Test.Q1)
async def continue_test(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(name=answer)
    await message.answer("What's your email?")
    await Test.Q2.set()


@dp.message_handler(state=Test.Q2)
async def finally_test(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(email=answer)
    await message.answer("What's your phone number?")
    await Test.Q3.set()


@dp.message_handler(state=Test.Q3)
async def last_report(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(phone=answer)

    data = await state.get_data()
    name = data.get("name")
    email = data.get("email")
    phone = data.get("phone")

    await message.answer("Привет! Ты ввел следующие данные:\n\n"
                         f"Имя - \"{name}\"\n\n"
                         f"Email - \"{email}\"\n\n"
                         f"Телефон: - \"{phone}\"")
    await state.reset_state()
