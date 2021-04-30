from aiogram import types
from aiogram.types import ReplyKeyboardRemove, CallbackQuery
from aiogram.utils.markdown import hitalic

from items.banking.banking import regional_banking
from keyboards.inline.callback_datas import industries_callback, set_asset_callback

from items.energy.energy_sector import energy
from items.finance.finance import finance
from items.tecnhologies.technologies import technologies
from items.real_estate.real_estate import real_estate
from items.russian_market.russian_market import russian_market
from items.developed_markets.markets import developed_markets
# BANKING, ENERGY, FINANCE, TECHNOLOGIES, REAL ESTATE, RUSSIAN MARKET, DEVELOPED MARKETS

from keyboards.inline.robo_markups import industries_markup, get_chosen_sectors, set_asset_markup

from loader import dp
from states import PortfolioStates
from aiogram.dispatcher import FSMContext

'''
@dp.message_handler(text="Перейти к робоэдвайзеру", state=PortfolioStates.Continue_After_Start)
async def forming_portfolio(message: types.Message, state: FSMContext):
    await message.answer("Перед моделированием ребалансировки портфеля робоэдвайзер соберет информацию по поводу "
                         "бюджета, состава инвестиционного портфеля и индивидуальных предпочтений относительно "
                         "ребалансирования", reply_markup=ReplyKeyboardRemove())
    await message.answer("Начать составление портфеля акций?", reply_markup=yes_markup)
    await PortfolioStates.Set_Budget.set()


@dp.message_handler(state=PortfolioStates.Set_Budget)
async def get_budget(message: types.Message, state: FSMContext):
    await message.answer("Введите сумму, которую вы планируете инвестировать в долларах США (минимальная сумма 20.000):"
                         , reply_markup=ReplyKeyboardRemove())
    await PortfolioStates.Check_Budget.set()
'''


@dp.message_handler(state=PortfolioStates.Check_Budget)
async def check_budget(message: types.Message, state: FSMContext):
    await state.reset_state()
    budget = message.text
    if budget.isdigit() and int(budget) >= 20000:
        await state.update_data(budget=int(budget))
        await message.answer(f"Выберите отрасли, в которые вы бы хотели инвестировать:", reply_markup=industries_markup)
    else:
        await message.answer("Вы ввели некорректный формат бюджета. Наиболее частые ошибки:\n\n"
                             "§ Наличие пунктуации (\"120.000\", \"50,200\")\n"
                             "§ Наличие знаков, отличных от цифр (\"30 000$\", \"15000 USD D\")\n"
                             "§ Бюджет меньше минимально требуемого (\"5000\",\"19900\")")
        await message.answer("Введите сумму, которую вы планируете инвестировать в долларах США"
                             " (минимальная сумма 20.000):")
        await PortfolioStates.Check_Budget.set()


@dp.callback_query_handler(industries_callback.filter(button_name="Закончить. Выбрано -> "))
async def finish_choosing_industries(call: CallbackQuery, callback_data: dict):
    chosen_sectors = get_chosen_sectors(industries_markup)
    #  await call.answer(f"chosen sectors len = {industries_markup.inline_keyboard[0][0]}", show_alert=True)
    if len(chosen_sectors) < 2:
        await call.answer("Выберите минимум 2 класса активов, из предложенных в списке", show_alert=True)
    else:
        final_list = ""
        for j in range(len(chosen_sectors)):
            final_list = final_list + str(j + 1) + ". " + chosen_sectors[j] + "\n"
        await call.message.edit_text("Выбранные секторы:\n" + hitalic(f"{final_list}"))
        await call.bot.send_message(text="Выберите пропорции между указанными активами:", chat_id=call.message.chat.id,
                                    reply_markup=set_asset_markup)
        await call.message.edit_reply_markup()


@dp.callback_query_handler(industries_callback.filter())
async def choosing_industries(call: CallbackQuery, callback_data: dict):
    button_name = callback_data.get("button_name")
    is_chosen = int(callback_data.get("is_chosen"))
    button_id = int(callback_data.get("button_id"))
    change_sum_parameter = 1

    if is_chosen == 0:  # is not chosen
        await call.answer(f"Сектор {button_name} добавлен в портфель", show_alert=False)
        industries_markup.inline_keyboard[button_id][0].callback_data = industries_callback.new(button_name=button_name,
                                                                                                is_chosen=1,
                                                                                                button_id=button_id)
        industries_markup.inline_keyboard[button_id][0].text = button_name + " ☑️"
    else:
        await call.answer(f"Сектор {button_name} был исключен из портфеля", show_alert=False)
        industries_markup.inline_keyboard[button_id][0].callback_data = industries_callback.new(button_name=button_name,
                                                                                                is_chosen=0,
                                                                                                button_id=button_id)
        industries_markup.inline_keyboard[button_id][0].text = button_name
        change_sum_parameter = -1

    last_button_text = industries_markup.inline_keyboard[7][0].text
    industries_markup.inline_keyboard[7][0].text = last_button_text.split(':')[0] + ': '\
                                                   + str(int(last_button_text.split(':')[1]) + change_sum_parameter)

    await call.message.edit_reply_markup(reply_markup=industries_markup)


@dp.callback_query_handler(set_asset_callback.filter(action="поделить поровну"))
async def divide_budget(call: CallbackQuery, callback_data: dict):
    chosen_variant = set_asset_markup.inline_keyboard[0][0].text
    await call.message.edit_text("Выберите пропорции между указанными активами:\n" + hitalic("-" + chosen_variant))
    await call.message.edit_reply_markup()



@dp.callback_query_handler(set_asset_callback.filter(action="свои пропорции"))
async def divide_budget(call: CallbackQuery, callback_data: dict):
    chosen_variant = set_asset_markup.inline_keyboard[1][0].text
    await call.message.edit_text("Выберите пропорции между указанными активами:\n" + hitalic("-" + chosen_variant))
    await call.message.edit_reply_markup()

'''
    if button_id == 0:  # if button is not chosen
        await call.answer(f"Сектор {button_name} добавлен в портфель", show_alert=False)
        industries_markup.inline_keyboard[0][button_id].text = button_name + " ☑️"
        industries_markup.inline_keyboard[0][button_id].callback_data.split(':')[1] = 
    industries_markup.inline_keyboard[0][0].callback_data.split(':')[1]
    await dp.bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                           reply_markup=industries_markup)
    # dp.bot.edit_message_reply_markup()
'''

'''
@dp.callback_query_handler(product_callback.filter(action="buy"))
async def buying_product(call: CallbackQuery, callback_data: dict):
    product_id = callback_data.get("id")
    await call.message.edit_caption(f"Покупай товар номер {product_id}!")
    await call.message.edit_reply_markup()
'''

'''
@dp.message_handler(state=PortfolioStates.Continue_After_Start)
async def continue_test(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(name=answer)

    data = await state.get_data()
    name = data.get("name")
    await message.answer(f'{name} ++++')
    #await Test.Q2.set()
'''
# await dp.bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=industries_markup)
