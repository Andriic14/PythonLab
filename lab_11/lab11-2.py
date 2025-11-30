import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)
plt.style.use('ggplot')
plt.rcParams['figure.figsize'] = (15, 5)
try:
    df = pd.read_csv('comptagevelo2009.csv', sep=',',parse_dates=['Date'],dayfirst=True,index_col='Date')
except KeyError:
    df = pd.read_csv('comptagevelo2009.csv',sep = ',',parse_dates=True)
    pass
print("Інформація про DataFrame")
df.info()
print("-" * 40)
df = df.fillna(0)
numeric_df = df.select_dtypes(include=['number'])
print("Описова статистика")
print(numeric_df.describe())
print("-" * 40)
total_cyclists_all_paths = numeric_df.sum().sum()
print(f"Загальна кількість велосипедистів за рік (2009) на усіх велодоріжках: {total_cyclists_all_paths:,.0f}")
print("-" * 40)
total_cyclists_per_path = numeric_df.sum().sort_values(ascending=False)
print("Загальна кількість велосипедистів за рік на кожній велодоріжці:")
print(total_cyclists_per_path)
print("-" * 40)
selected_paths = ['Berri1','Maisonneuve_1','Maisonneuve_2']
monthly_totals = numeric_df.groupby(numeric_df.index.month).sum()
selected_monthly_totals = monthly_totals[selected_paths]
most_popular_month = selected_monthly_totals.idxmax()
month_name = {1: 'Січень', 2: 'Лютий', 3: 'Березень', 4: 'Квітень', 5: 'Травень', 6: 'Червень', 7: 'Липень', 8: 'Серпень', 9: 'Вересень', 10: 'Жовтень', 11: 'Листопад', 12: 'Грудень'}
print("Найбільш популярний місяць на обраних велодоріжках:")
print(most_popular_month.map(month_name))
print("-" * 40)
path_to_plot = 'Berri1'
plt.figure(figsize = (15, 5))
monthly_totals[path_to_plot].plot(kind='line',marker='o')
plt.title(f'Завантаженість велодоріжки "{path_to_plot}" по місяцях (2009)')
plt.xlabel('Місяць')
plt.ylabel('Загальна кількість велосипедистів')
plt.xticks(range(1,13))
plt.grid(True)
plt.show()
print(f"Графік завантаженості велодоріжки '{path_to_plot}' побудовано.")
print("-" * 40)