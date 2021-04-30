import pandas as pd
import pathlib

finance = pd.read_csv("/Users/home/PycharmProjects/udemy_course/items/finance/Alerian MLP ETF (AMLP).csv")

del finance["Откр."]
del finance["Макс."]
del finance["Мин."]
del finance["Объём"]
del finance["Изм. %"]

finance.rename(columns={'Дата': 'Date', 'Цена': 'Price'}, inplace=True)
finance['Price'] = finance['Price'].str.replace(',', '.')

finance['Date'] = pd.to_datetime(finance['Date'])
finance['Price'] = pd.to_numeric(finance['Price'])


