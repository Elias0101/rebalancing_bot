from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart, Command
from aiogram.types import ReplyKeyboardRemove

from keyboards.default import yes_markup
from loader import dp
from states import PortfolioStates


@dp.message_handler(CommandStart("start"))
async def bot_start(message: types.Message):
    await message.answer(f'Добрый день, {message.from_user.full_name}.\n\n'
                         'Вы вступили в переписку с робоэдвайзером, который помогает осуществлять ребалансировку'
                         ' инвестиционного портфеля, состоящего из ценных бумаг\n\n'
                         'Чат-бот использует модельные данные по акциям из {источник} ***\n\n'
                         'По вопросам, связанным с робоэвдайзером, можно обращаться'
                         ' к основателю проекта @elais_loladze')
    #await message.answer("Перейти к робоэдвайзеру?", reply_markup=yes_markup)
    await PortfolioStates.Set_Budget.set()
    #await message.answer(f'Привет, {message.from_user.full_name}!')


@dp.message_handler(Command("start"))
async def bot_start(message: types.Message):
    await message.answer(f'Добрый день, {message.from_user.full_name}.\n\n'
                         'Вы вступили в переписку с робоэдвайзером, который помогает осуществлять ребалансировку'
                         ' инвестиционного портфеля, состоящего из ценных бумаг\n\n'
                         'Чат-бот использует модельные данные по акциям из {источник} ***\n\n'
                         'По вопросам, связанным с робоэвдайзером, можно обращаться'
                         ' к основателю проекта @elais_loladze')
    #await message.answer("Перейти к робоэдвайзеру?", reply_markup=yes_markup)
    await message.answer("Введите сумму, которую вы планируете инвестировать в долларах США (минимальная сумма 20.000):"
                         , reply_markup=ReplyKeyboardRemove())
    await PortfolioStates.Check_Budget.set()

'''
@dp.message_handler(text="Перейти к робоэдвайзеру")
async def get_bugdet(message: types.Message):
    await message.answer("Starting", reply_markup=ReplyKeyboardRemove())
'''
