import types

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.callback_datas import product_callback

def create_edit_markup(product, id):
    edit_markup = InlineKeyboardMarkup(row_width=3,
                                       inline_keyboard=[
                                           [
                                               InlineKeyboardButton(
                                                   text="Купить товар",
                                                   callback_data=product_callback.new(action="buy", product=product, id=id)
                                               )
                                           ],
                                           [
                                               InlineKeyboardButton(
                                                   text="👍",
                                                   callback_data=product_callback.new(action="like", product=product, id=id)
                                               ),
                                               InlineKeyboardButton(
                                                   text="👎",
                                                   callback_data=product_callback.new(action="deslike", product=product, id=id)
                                               )
                                           ],
                                           [
                                               InlineKeyboardButton(
                                                   text="Поделиться с другом",
                                                   switch_inline_query="@elais_test_bot"
                                               )
                                           ]
                                       ])
    return edit_markup


'''  
edit_markup = InlineKeyboardMarkup(row_width=3,
                                   inline_keyboard=[
                                       [
                                           InlineKeyboardMarkup(
                                               text="Купить товар",
                                               callback_data=product_callback.new(action="buy")
                                           )
                                       ],
                                       [
                                           InlineKeyboardMarkup(
                                               text="👍",
                                               callback_data=product_callback.new(action="like")
                                           ),
                                           InlineKeyboardMarkup(
                                               text="👎",
                                               callback_data=product_callback.new(action="deslike")
                                           )
                                       ],
                                       [
                                           InlineKeyboardMarkup(
                                               text="Поделиться с другом",
                                               callback_data=product_callback.new(action="share")
                                           )
                                       ]
                                   ])
'''