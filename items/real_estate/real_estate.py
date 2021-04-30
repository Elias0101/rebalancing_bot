import pandas as pd
import pathlib

real_estate = pd.read_csv("/Users/home/PycharmProjects/udemy_course/items/real_estate/SPDR S&P Homebuilders ETF (XHB).csv")

del real_estate["Откр."]
del real_estate["Макс."]
del real_estate["Мин."]
del real_estate["Объём"]
del real_estate["Изм. %"]

real_estate.rename(columns={'Дата': 'Date', 'Цена': 'Price'}, inplace=True)
real_estate['Price'] = real_estate['Price'].str.replace(',', '.')

real_estate['Date'] = pd.to_datetime(real_estate['Date'])
real_estate['Price'] = pd.to_numeric(real_estate['Price'])




