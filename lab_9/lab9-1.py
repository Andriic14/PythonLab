import csv
import os
print("Inflation, consumer prices для України за 1991-2019 роки")
filename = "API_FP.CPI.TOTL.ZG_DS2_en_csv_v2_242560.csv"
try:
    csvfile =open(filename,"r",encoding="utf-8")
    for _ in range(4):
        next(csvfile)
    reader=csv.DictReader(csvfile ,delimiter=",")# Створюємо reader для читання CSV як словників
    print("\nДані про інфлацію в Україні")
    print("Рік : Інфляція (%)")
    years = [str(year) for year in range(1991,2020)]# Список років з 1991 по 2019
    for row in reader: # Виводимо всі дані на екран
        if row.get("Country Name") == "Ukraine":
            for year in years:
                inflation_value = row.get(year,"")# Отримуємо значення інфляції за рік
                if inflation_value and inflation_value.strip(): # Виводимо лише якщо значення не пусте
                    try:
                        formatted_value = float(inflation_value)
                        print(f"{year:<10} {formatted_value:>20.2f}")
                    except ValueError:
                        print(f"{year:<10} {inflation_value:>20.2f}")# Якщо не вдалося перетворити на число
    csvfile .close()
    print("Дані прочитані")
except FileNotFoundError:
    print("Помилка. Файл 'API.FP.CPI.TOTL.ZG_DS2_en_csv_v2_242560.csv' не знайдено")
    exit()
except Exception as e:
    print(f"Виникла помилка при читанні файлу: {e}")
    exit()

try:
    csvfile=open(filename,"r",encoding="utf-8")# Відкриваємо файл заново для пошуку мін/макс значень
    for _ in range(4):
        next(csvfile)
    reader=csv.DictReader(csvfile,delimiter=",")
    # Змінні для зберігання мін/макс значень
    min_inflation =float('inf')
    max_inflation = float('-inf')
    min_year = ""
    max_year = ""
    print("Пошук найнижчого та найвищого значень")
    # Список років для аналізу
    years = [str(year) for year in range(1991, 2020)]
    for row in reader:
        if row.get("Country Name") == "Ukraine":# Шукаємо рядок з даними для України
            for year in years:# Перевіряємо кожен рік
                inflation_value = row.get(year,"")
                # Якщо значення не пусте, обробляємо його
                if inflation_value and inflation_value.strip():
                    try:
                        # Перетворюємо текст на число
                        inflation_value = float(inflation_value)
                        # Перевіряємо, чи це новий мінімум
                        if inflation_value < min_inflation:
                            min_inflation = inflation_value
                            min_year = year
                            # Перевіряємо, чи це новий максимум
                        if inflation_value > max_inflation:
                            max_inflation = inflation_value
                            max_year = year
                    except ValueError:
                        continue
    csvfile.close()
    # Виводимо результати
    print(f"\nНайнижча інфляція: {min_inflation}% у {min_year} році")
    print(f"Найвища інфляція: {max_inflation}% у {max_year} році")

    print("Збереження результатів")
    with open("inflation_results.csv","w",encoding="utf-8",newline='') as result_file:
        writer = csv.writer(result_file, delimiter=";") # Створюємо writer для запису
        writer.writerow(["Показник","Значення (%)","Рік"])# Записуємо заголовок
        writer.writerow(["Найнижча інфляція", min_inflation, min_year])
        writer.writerow(["Найвища інфляція", max_inflation, max_year])
    print("\nРезультати збережено у файл 'inflation_results.csv'")
    print("Програма завершина")
except FileNotFoundError:
    print("Помилка файл 'inflation_results.csv' не знайдено")
except Exception as e:
    print(f"Виникла помилка: {e}")
