import pandas as pd
import pathlib

technologies = pd.read_csv("/Users/home/PycharmProjects/udemy_course/items/tecnhologies/Technology Select Sector SPDR Fund (XLK).csv")

del technologies["Откр."]
del technologies["Макс."]
del technologies["Мин."]
del technologies["Объём"]
del technologies["Изм. %"]

technologies.rename(columns={'Дата': 'Date', 'Цена': 'Price'}, inplace=True)
technologies['Price'] = technologies['Price'].str.replace(',', '.')

technologies['Date'] = pd.to_datetime(technologies['Date'])
technologies['Price'] = pd.to_numeric(technologies['Price'])


