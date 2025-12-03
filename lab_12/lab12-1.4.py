import dask.dataframe as dd
import pandas as pd

# Створення великого датасету (симуляція)
# У реальності Dask читає дані з файлів партіями
large_data = pd.DataFrame({
    'id': range(1000000),
    'value': range(1000000),
    'category': ['A', 'B', 'C', 'D'] * 250000
})

# Конвертація в Dask DataFrame
ddf = dd.from_pandas(large_data, npartitions=4)

# Операції виконуються паралельно
result = ddf.groupby('category')['value'].mean()

# Фактичне обчислення відбувається при виклику compute()
computed_result = result.compute()
print("Середнє значення по категоріях:")
print(computed_result)

# Складні операції з великими даними
filtered = ddf[ddf['value'] > 500000]
aggregated = filtered.groupby('category').agg({
    'value': ['mean', 'sum', 'count']
})

# Візуалізація графу обчислень (опційно)
# aggregated.visualize()

final_result = aggregated.compute()
print("\nАгреговані дані:")
print(final_result)