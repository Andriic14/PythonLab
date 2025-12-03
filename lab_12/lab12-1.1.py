import numpy as np

# Створення масиву даних про продажі
sales = np.array([120, 150, 180, 200, 170, 190, 210])

# Статистичні обчислення
print(f"Середні продажі: {np.mean(sales):.2f}")
print(f"Стандартне відхилення: {np.std(sales):.2f}")

# Векторизовані операції - збільшення на 10%
increased_sales = sales * 1.1
print(f"Прогноз продажів: {increased_sales}")

# Робота з двовимірними даними (матриця продажів по регіонах)
sales_matrix = np.array([
    [120, 150, 180],  # Регіон 1
    [200, 170, 190],  # Регіон 2
    [210, 220, 240]   # Регіон 3
])

# Сума по стовпцях (місяці)
monthly_totals = np.sum(sales_matrix, axis=0)
print(f"Загальні продажі по місяцях: {monthly_totals}")

# Сума по рядках (регіони)
regional_totals = np.sum(sales_matrix, axis=1)
print(f"Загальні продажі по регіонах: {regional_totals}")
