import pandas as pd
import pathlib

regional_banking = pd.read_csv('/Users/home/PycharmProjects/udemy_course/items/banking/SPDR S&P Regional Banking ETF (KRE).csv')

#pd.read_csv("Users/home//udemy_course/items/banking/SPDR S&P Regional Banking ETF (KRE).csv")

#pd.read_csv(str(pathlib.Path.cwd()) + "/" +"SPDR S&P Regional Banking ETF (KRE).csv")

del regional_banking["Откр."]
del regional_banking["Макс."]
del regional_banking["Мин."]
del regional_banking["Объём"]
del regional_banking["Изм. %"]

regional_banking.rename(columns={'Дата': 'Date', 'Цена': 'Price'}, inplace=True)
regional_banking['Price'] = regional_banking['Price'].str.replace(',', '.')

regional_banking['Date'] = pd.to_datetime(regional_banking['Date'])
regional_banking['Price'] = pd.to_numeric(regional_banking['Price'])

'''
print(regional_banking.head())
print(regional_banking.info)
print(regional_banking.dtypes)
'''
#print(str(pathlib.Path.cwd()))