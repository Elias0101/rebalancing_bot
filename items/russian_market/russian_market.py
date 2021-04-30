import pandas as pd
import pathlib

russian_market = pd.read_csv("/Users/home/PycharmProjects/udemy_course/items/russian_market/VanEck Vectors Russia ETF (RSX).csv")

del russian_market["Откр."]
del russian_market["Макс."]
del russian_market["Мин."]
del russian_market["Объём"]
del russian_market["Изм. %"]

russian_market.rename(columns={'Дата': 'Date', 'Цена': 'Price'}, inplace=True)
russian_market['Price'] = russian_market['Price'].str.replace(',', '.')

russian_market['Date'] = pd.to_datetime(russian_market['Date'])
russian_market['Price'] = pd.to_numeric(russian_market['Price'])


