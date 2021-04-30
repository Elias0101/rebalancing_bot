import pandas as pd
import pathlib

developed_markets = pd.read_csv("/Users/home/PycharmProjects/udemy_course/items/developed_markets/Vanguard FTSE Developed Markets Index Fund ETF Shares (VEA).csv")

del developed_markets["Откр."]
del developed_markets["Макс."]
del developed_markets["Мин."]
del developed_markets["Объём"]
del developed_markets["Изм. %"]

developed_markets.rename(columns={'Дата': 'Date', 'Цена': 'Price'}, inplace=True)
developed_markets['Price'] = developed_markets['Price'].str.replace(',', '.')

developed_markets['Date'] = pd.to_datetime(developed_markets['Date'])
developed_markets['Price'] = pd.to_numeric(developed_markets['Price'])

