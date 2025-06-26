import pandas as pd

# Загружаем CSV
df = pd.read_csv("../csv/employees.csv")

# Самый простой способ через индексы
full_names = [df['first_name'][i] + ' ' + df['last_name'][i] for i in range(len(df))]
print("All names:", full_names)

# Фильтрация по букве 'e'
names_with_e = [name for name in full_names if 'e' in name.lower()]
print("Names with 'e':", names_with_e)