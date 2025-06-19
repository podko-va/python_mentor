import plotly.express as px
import plotly.data as pldata


def strength_to_float(s):
    s = s.replace('+', '')  # убрать знак +, если есть
    if '-' in s:
        parts = s.split('-')
        low = float(parts[0])
        high = float(parts[1])
        return (low + high) / 2
    else:
        return float(s)
# Загрузка данных о ветре в DataFrame
df = pldata.wind(return_type='pandas')

# Печать первых и последних 10 строк для проверки
# print(df.head(10))
# print(df.tail(10))

# unique_values = df['strength'].unique()
# print(unique_values)


df['strength_float'] = df['strength'].apply(strength_to_float)
# print(df.head(10))
# # Очистка данных: убираем знак % и конвертируем в float
# df['strength'] = df['strength'].str.replace('%', '', regex=False)
# df['strength'] = df['strength'].astype(float)

# Создаем интерактивный scatter plot
fig = px.scatter(
    df,
    x='strength_float',
    y='frequency',
    color='direction',
    title='Wind Strength vs Frequency by Direction',
    labels={'strength_float': 'Strength', 'frequency': 'Frequency'}
)

# Сохраняем в HTML и автоматически открываем в браузере
fig.write_html('wind.html', auto_open=True)
