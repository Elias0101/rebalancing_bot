from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.callback_datas import industries_callback, set_asset_callback


#from callback_datas import industries_callback


# BANKING, ENERGY, FINANCE, TECHNOLOGIES, REAL ESTATE, RUSSIAN MARKET, DEVELOPED MARKETS

# industries_callback = CallbackData("item", "button_name", "is_chosen")

def get_chosen_sectors(markup):
    chosen_sectors = []
    for i in range(7):
        # "item", "button_name", "is_chosen", "button_id"
        if int(markup.inline_keyboard[i][0].callback_data.split(':')[2]) == 1:
            chosen_sectors.append(markup.inline_keyboard[i][0].callback_data.split(':')[1])
    return chosen_sectors


def reset_industry_markup(markup, callback_data):
    for i in range(7):
        # "item", "button_name", "is_chosen", "button_id"
        if int(markup.inline_keyboard[i][0].callback_data.split(':')[2]) == 1:
            button_name = callback_data.get("button_name")
            button_id = int(callback_data.get("button_id"))
            markup.inline_keyboard[i][0].callback_data = industries_callback.new(button_name=button_name, is_chosen=0, button_id=button_id)
            markup.inline_keyboard[i][0].text = button_name
    industries_markup.inline_keyboard[7][0].text = "Закончить. Выбрано: 0"
    return industries_markup


industries_markup = InlineKeyboardMarkup(row_width=2,
                                         inline_keyboard=[
                                             [
                                                 InlineKeyboardButton(
                                                     text="Banking",
                                                     callback_data=industries_callback.new(button_name="Banking", is_chosen=0, button_id=0)
                                                 )
                                             ],
                                             [
                                                 InlineKeyboardButton(
                                                     text="Energy",
                                                     callback_data=industries_callback.new(button_name="Energy", is_chosen=0, button_id=1)
                                                 )
                                             ],
                                             [
                                                 InlineKeyboardButton(
                                                     text="Finance",
                                                     callback_data=industries_callback.new(button_name="Finance", is_chosen=0, button_id=2)
                                                 )
                                             ],
                                             [
                                                 InlineKeyboardButton(
                                                     text="Technologies",
                                                     callback_data=industries_callback.new(button_name="Technologies", is_chosen=0, button_id=3)
                                                 )
                                             ],
                                             [
                                                 InlineKeyboardButton(
                                                     text="Real Estate",
                                                     callback_data=industries_callback.new(button_name="Real Estate", is_chosen=0, button_id=4)
                                                 )
                                             ],
                                             [
                                                 InlineKeyboardButton(
                                                     text="Russian Market",
                                                     callback_data=industries_callback.new(button_name="Russian Market", is_chosen= 0, button_id=5)
                                                 )
                                             ],
                                             [
                                                 InlineKeyboardButton(
                                                     text="Developed Markets",
                                                     callback_data=industries_callback.new(button_name="Developed Markets", is_chosen=0, button_id=6)
                                                 )
                                             ],
                                             [
                                                 InlineKeyboardButton(
                                                     text="Закончить. Выбрано: 0",
                                                     callback_data=industries_callback.new(button_name="Закончить. Выбрано -> ", is_chosen=0, button_id=7)
                                                 )
                                             ]
                                         ], resize_keyboard=True)

set_asset_markup = InlineKeyboardMarkup(row_width=2,
                                        inline_keyboard=[
                                            [
                                                InlineKeyboardButton(
                                                    text="Поделить бюджет поровну",
                                                    callback_data=set_asset_callback.new(action="поделить поровну")
                                                )
                                            ],
                                            [
                                                InlineKeyboardButton(
                                                    text="Задать свои пропорции",
                                                    callback_data=set_asset_callback.new(action="свои пропорции")
                                                )
                                            ]
                                        ], resize_keyboard=True)


#industries_markup.inline_keyboard[0][0].text = "Banking (1)"

#industries_markup.inline_keyboard[0][0].callback_data = industries_callback.new(button_name="Banking", is_chosen=1, button_id=0)

#print(str(industries_markup.inline_keyboard[7][0]))  # item:Banking:0:0


#print(industries_markup.inline_keyboard[0][0])

