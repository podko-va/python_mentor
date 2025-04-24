# replace()
import pandas as pd
df = pd.DataFrame({'A': [1, 2, 'N/A', 4]})
df['A'] = df['A'].replace('N/A', pd.NA)
print(df)

# to_numeric()
df = pd.Series(['1', '2', '3', 'N/A'])
df = pd.to_numeric(df, errors='coerce')  # Преобразуем в числа, N/A заменим на NaN
print(df)

# fillna()
df = pd.DataFrame({'A': [1, 2, None, 4]})
df['A'] = df['A'].fillna(df['A'].mean())  # Заполняем NaN средним значением
print(df)

# ffill() и bfill()
df = pd.DataFrame({'A': [1, None, 3, None, 5]})
df['A'] = df['A'].ffill()  # Заполняем пропуски значениями вперед
print(df)

# series.str
df = pd.Series(['apple', 'banana', 'grape', 'apple pie'])
df = df[df.str.contains('apple')]  # Фильтрация строк, содержащих 'apple'
print(df)

# to_datetime()
df = pd.Series(['2021-01-01', '2021-02-01', '2021-03-01'])
df = pd.to_datetime(df)
print(df)

# astype()
import pandas as pd
data = {'A': ['1', '2', '3', '4']}
df = pd.DataFrame(data)
print(df.dtypes)
df['A'] = df['A'].astype(int)
print(df.dtypes)
print(df)