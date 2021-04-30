from aiogram.types import InlineKeyboardMarkup

from keyboards.inline.callback_datas import edit_callback

edit_markup = InlineKeyboardMarkup(row_width=2,
                                   inline_keyboard=[
                                       [
                                           InlineKeyboardMarkup(
                                               text="Edit Name",
                                               callback_data=edit_callback.new(item_name="name")
                                           ),
                                               InlineKeyboardMarkup(
                                               text="Edit Description",
                                               callback_data=edit_callback.new(item_name="description")
                                           )
                                       ],
                                       [
                                           InlineKeyboardMarkup(
                                               text="Edit About",
                                               callback_data=edit_callback.new(item_name="about")
                                           ),
                                               InlineKeyboardMarkup(
                                               text="Edit Botpic",
                                               callback_data=edit_callback.new(item_name="botpic")
                                           )
                                       ],
                                       [
                                           InlineKeyboardMarkup(
                                               text="Edit Commands",
                                               callback_data=edit_callback.new(item_name="commands")
                                           ),
                                           InlineKeyboardMarkup(
                                               text="<<Back to Bot",
                                               callback_data=edit_callback.new(item_name="cancel")
                                           )
                                       ]
                                   ])