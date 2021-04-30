from aiogram.utils.callback_data import CallbackData

edit_callback = CallbackData("edit", "item_name")

product_callback = CallbackData("item", "action", "product", "id")

industries_callback = CallbackData("item", "button_name", "is_chosen", "button_id")

set_asset_callback = CallbackData("item", "action")
