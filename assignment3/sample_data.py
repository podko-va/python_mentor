import pandas as pd
import numpy as np

data = {
    'date': ['2021-01-01', '2021-02-01', '2021-03-01', '2021-04-01', '2021-05-01', '2021-06-01', '2021-07-01', '2021-08-01', '2021-09-01', '2021-10-01'],
    'product_name': ['Laptop', 'Phone', 'Tablet', 'Laptop', 'Phone', 'Tablet', 'Laptop', 'Phone', 'Tablet', 'Laptop'],
    'quantity': [10, 15, 20, 12, 18, 22, 8, 14, 19, 11],
    'unit_price': [1000, 500, 300, 1000, 500, 300, 1000, 500, 300, 1000],
    'total_price': [10000, 7500, 6000, 12000, 9000, 6600, 8000, 7000, 5700, 11000],
    'seller_name': ['Alice', 'Bob', 'Charlie', 'Alice', 'Bob', 'Charlie', 'Alice', 'Bob', 'Charlie', 'Alice'],
    'region': ['North', 'South', 'East', 'West', 'North', 'South', 'East', 'West', 'North', 'South']
}

df = pd.DataFrame(data)

# ошибки 
df.loc[2, 'date'] = '2021-03-32'  # Неверная дата
df.loc[5, 'unit_price'] = None  # Отсутствие цены за единицу
df.loc[7, 'total_price'] = pd.NA  # Некорректная общая стоимость


file_path = 'sales_data.csv'
df.to_csv(file_path, index=False)

# Добавляем пропущенные строки
df.loc[3] = [None, None, None, None, None, None, None]  # Полностью пустая строка
df.loc[8] = [None, 'Phone', None, None, None, 'Bob', 'South']  # Пропущенные данные в некоторых столбцах

# Добавляем дубликаты строк
df = pd.concat([df, df], ignore_index=True)
# Строка, которую нужно добавить в конец
new_row = ['2021-06-01', 'Phone', 18, 500, 9000, 'Bob', 'South']

# Добавляем строку в конец DataFrame
df.loc[len(df)] = new_row

# Сохраняем обновленные данные в CSV файл
file_path_with_errors = 'sales_data_with_errors.csv'
df.to_csv(file_path_with_errors, index=False)

print(df.tail(10))

sample_dropping = df.drop_duplicates(subset='product_name', keep='last')
#df.drop_duplicates(subset='product_name', inplace=True)
print("sample_dropping",'\n',sample_dropping)

sample_dropping1 = df.drop_duplicates()
#df.drop_duplicates(subset='product_name', inplace=True)
print("sample_dropping1",'\n',sample_dropping1, len(df), len(sample_dropping1))