import pandas as pd
import pathlib

energy = pd.read_csv("/Users/home/PycharmProjects/udemy_course/items/energy/Energy Select Sector SPDR® Fund (XLE).csv")

del energy["Откр."]
del energy["Макс."]
del energy["Мин."]
del energy["Объём"]
del energy["Изм. %"]

energy.rename(columns={'Дата': 'Date', 'Цена': 'Price'}, inplace=True)
energy['Price'] = energy['Price'].str.replace(',', '.')

energy['Date'] = pd.to_datetime(energy['Date'])
energy['Price'] = pd.to_numeric(energy['Price'])



