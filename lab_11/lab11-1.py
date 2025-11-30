import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)
df=pd.DataFrame({'Модель': ["Toyota Camry", "Honda Civic", "BMW X5", "Ford Focus", "Mercedes C-Class", "Mazda 3", "Audi A6", "Volkswagen Polo", "Lexus ES", "Hyundai Elantra"],
    'Потужність_КС': [150, 90, 250, 85, 180, 95, 200, 75, 160, 105],
    'Ціна_USD': [25000, 18000, 55000, 15000, 45000, 20000, 50000, 12000, 40000, 19000],
    'Кількість_Проданих': [10, 15, 3, 25, 5, 18, 4, 30, 6, 17],
    'Категорія': ['Седан', 'Седан', 'SUV', 'Хетчбек', 'Седан', 'Хетчбек', 'Седан', 'Хетчбек', 'Седан', 'Седан']})
print("Базовий аналіз")
print("Перші 3 рядки\n")
print(df.head(3))
print("-" * 40)
print("Типи даних")
print(df.dtypes)
print("-" * 40)
print("Кількість рядків і стовпців")
print(df.shape)
print("-" * 40)
print("Описова статистика")
print(df.describe())
print("-" * 40)

df['Загальна_Сума_Продажів'] = df['Ціна_USD'] * df['Кількість_Проданих']
print("DataFrame із доданим стовпцем 'Загальна_Сума_Продажів':")
print(df[['Модель', 'Ціна_USD', 'Кількість_Проданих', 'Загальна_Сума_Продажів']].head())
print("-" * 40)

try:
    price_threshold = int(input("Введіть максимальну ціну (USD) для фільтрації: "))
    filtered_df = df[df['Ціна_USD'] < price_threshold]
    print(f"\nРезультат фільтрації (Ціна менше {price_threshold} USD):")
    if filtered_df.empty:
        print("Не знайдено автомобілів, ціна яких менша за введений поріг")
    else:
        print(filtered_df)
except ValueError:
    print("\nПомилка: Будь ласка, введіть коректне числове значення")
print("-" * 40)

sort_df = df.sort_values(by='Ціна_USD',ascending=False)
print("DataFrame, відсортований за ціною (спадання):")
print(sort_df)
print("-" * 40)
category_mean = df.groupby('Категорія').mean(numeric_only=True)
print("Середнє значення за категоріями:")
print(category_mean)
print("-" * 40)
max_sales_by_category = df.groupby('Категорія')['Загальна_Сума_Продажів'].max()
print("Максимальна сума продажів у кожній категорії:")
print(max_sales_by_category)
print("-" * 40)

