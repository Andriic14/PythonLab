import pandas as pd

# Створення DataFrame з даними про продукти
data = {
    'product': ['Laptop', 'Mouse', 'Keyboard', 'Monitor', 'Laptop'],
    'category': ['Electronics', 'Accessories', 'Accessories', 'Electronics', 'Electronics'],
    'price': [1200, 25, 75, 300, 1100],
    'quantity': [5, 50, 30, 10, 3],
    'date': ['2024-01-15', '2024-01-16', '2024-01-16', '2024-01-17', '2024-01-18']
}

df = pd.DataFrame(data)

# Конвертація дати
df['date'] = pd.to_datetime(df['date'])

# Додавання обчисленого стовпця
df['total'] = df['price'] * df['quantity']

print("Дані про продажі:")
print(df)

# Групування та агрегація
category_stats = df.groupby('category').agg({
    'total': 'sum',
    'quantity': 'sum',
    'price': 'mean'
}).round(2)

print("\nСтатистика по категоріях:")
print(category_stats)

# Фільтрація даних
expensive_items = df[df['price'] > 100]
print(f"\nДорогі товари (ціна > 100):\n{expensive_items}")

# Обробка пропущених даних
df_with_missing = df.copy()
df_with_missing.loc[2, 'price'] = None
df_filled = df_with_missing.fillna(df_with_missing['price'].mean())