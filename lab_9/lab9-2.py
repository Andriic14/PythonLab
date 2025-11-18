import json
import os


# Налаштування файлів та цін
DATA_FILE = "workshop_data.json"
RESULT_FILE = "weekly_cost_results.json"
def load_data():
    if not os.path.exists(DATA_FILE):
        print(f"Файл '{DATA_FILE}' не знайдено. Створюється базова структура")
        initial_data = {
            "Part_Prices":{
                "Type_A": 15.50,
                "Type_B": 4.25,
                "Type_C": 8.00,
                "Type_D": 22.10,
                "Type_E": 1.50
            },
            "Weekly_Production":[
                {"Day": "Понеділок", "Type_A": 100, "Type_B": 250, "Type_C": 50, "Type_D": 10, "Type_E": 300},
                {"Day": "Вівторок", "Type_A": 110, "Type_B": 230, "Type_C": 60, "Type_D": 15, "Type_E": 310},
                {"Day": "Середа", "Type_A": 90, "Type_B": 260, "Type_C": 45, "Type_D": 12, "Type_E": 290},
                {"Day": "Четвер", "Type_A": 105, "Type_B": 240, "Type_C": 55, "Type_D": 20, "Type_E": 320},
                {"Day": "П'ятниця", "Type_A": 95, "Type_B": 270, "Type_C": 50, "Type_D": 18, "Type_E": 280},
                {"Day": "Субота", "Type_A": 50, "Type_B": 100, "Type_C": 20, "Type_D": 5, "Type_E": 150},
                {"Day": "Неділя", "Type_A": 0, "Type_B": 0, "Type_C": 0, "Type_D": 0, "Type_E": 0},
            ]
        }
        save_data(initial_data)
        return  initial_data
    with open(DATA_FILE, "r", encoding="utf-8") as file:
        try:
            return json.load(file)
        except json.decoder.JSONDecodeError:
            print(f"омилка читання JSON у файлі {DATA_FILE}")
            return {"Part_Prices":{}, "Weekly_Production":[]}
def save_data(data):
    try:
        with open(DATA_FILE, "w", encoding="utf-8") as file:
            json.dump(data,file,indent=4,ensure_ascii=False)
    except IOError as e:
        print(f"Помилка запису у файл {DATA_FILE}: {e}")
def display_data(data):
    if not data:
        print("\nФайл даних порожній")
        return
    print(f"Вміст файлу {DATA_FILE}")
    print("\nЦіни на деталі:")
    for part, price in data.get("Part_Prices").items():
        print(f"    > {part:<10}: {price:>6.2f} грн")
    print("\n2 Щоденне виробництво:")
    production = data.get("Weekly_Production")
    if production:
        header = "День"
        part_types = list(data["Part_Prices"].keys())
        for pt in part_types:
            header += f" | {pt:6}"
        print(header)
        for day_entry in production:
            row_str = f"{day_entry['Day']:<10}"
            for pt in part_types:
                row_str += f" | {day_entry.get(pt,0):<6}"
            print(row_str)
    else:
        print("Дані про виробництво відсутні")
def add_record(data):
        print("\nДодавання нового запису (дня тижня) до виробництва:")
        existing_days = {entry["Day"] for entry in data.get("Weekly_Production",[])} # Визначення назви нового дня
        while True:
            new_day = input("Введіть назву нового дня: ").strip()
            if new_day not in existing_days:
                break
            print(f"Некоректна назва або день '{new_day}' вже існує. Спробуйте іншу назву.")
        new_entry = {"Day": new_day }
        # Збір даних по випуску для всіх типів деталей
        for part_type in data["Part_Prices"].keys():
            while True:
                try:
                    count= int(input(f"Введіть кількість деталей {part_type}: "))
                    if count >= 0:
                        new_entry[part_type] = count
                        break
                    else:
                        print("Кількість не може бути від'ємною")
                except ValueError:
                    print("Некоректний ввід. Введіть ціле число")
        data["Weekly_Production"].append(new_entry)
        save_data(data)
        print(f"\nНовий запис для дня '{new_day}' додано")
def delete_record(data):
    production = data.get("Weekly_Production",[])
    if not production:
        print("\nНемає записів для видалення")
        return
    print("\nВидалення запису. Доступні дні:")
    for i, entry in enumerate(production):
        print(f"  {i+1}: {entry['Day']}")
    while True:
        try:
            choice = int(input("Введіть номер дня для видалення (або 0 для скасування): "))
            if choice == 0:
                print("Операцію скасовано")
                return
            if 1 <= choice <= len(production):
                deleted_day = production.pop(choice-1)['Day']
                save_data(data)
                print(f"\nЗапис для дня '{deleted_day}' успішно видалено")
                return
            else:
                print("Некоректний номер")
        except ValueError:
            print("Некоректний ввід. Введіть число")
def search_data(data):
    print("Пошук виробництва за днем тижня:")
    search_day = input("Введіть день тижня для пошуку: ").strip()
    production = data.get("Weekly_Production",[])
    found_entries = [
        entry for entry in production
        if entry ["Day"].lower() == search_day.lower()
    ]
    if found_entries:
        print(f"\nЗнайдено записи для дня '{search_day}':")
        for entry in found_entries:
            for key, value in entry.items():
                print(f"  {key:<12}: {value}")
    else:
        print(f"\nЗаписи для дня '{search_day}' не знайдено")
def calculate_weekly_cost(data):
    print("\nОбчислення загальної вартості деталей за тиждень")
    price = data.get("Part_Prices",{})
    production = data.get("Weekly_Production",[])
    if not price or not production:
        print("Недостатньо даних для обчислення")
        return
    total_weekly_cost = 0.0
    daily_cost = []
    #Обчислення вартості для кожного дня
    for day_entry in production:
        daily_total = 0.0
        # Обчислення вартості для кожного типу деталей
        for part_type, unit_price  in price.items():
            count = day_entry.get(part_type,0)
            cost = unit_price * count
            daily_total += cost
        total_weekly_cost += daily_total
        daily_cost.append({
            "Day":day_entry["Day"],
            "Details_By_Day":round(daily_total,2)
        })
    results = {
        "Total_Weekly_Cost_UAH":round(total_weekly_cost,2),
        "Cost_Per_Day":daily_cost
    }
    try:
        with open(RESULT_FILE, "w", encoding="utf-8") as file:
            json.dump(results,file,indent=4,ensure_ascii=False)
            print(f"\nЗагальна вартість за тиждень: {total_weekly_cost:.2f} грн.")
            print(f"Результати збережено у файл '{RESULT_FILE}'")
    except IOError as e:
        print(f"Помилка запису результатів: {e}")
def main_menu():
    print("Облік деталей та вартість")
    data=load_data()
    while True:
        print("\nОберіть опцію:")
        print("1 - Вивести на екран вміст JSON файлу")
        print("2 - Додати новий запис (день виробництва)")
        print("3 - Видалити запис (день виробництва)")
        print("4 - Пошук даних за днем тижня")
        print("5 - Визначити загальну вартість за тиждень")
        print("0 - Вихід")
        choice = input("Ваш вибір (0-5): ").strip()

        if choice == "1":
            display_data(data)
        elif choice == "2":
            add_record(data)
        elif choice == "3":
            delete_record(data)
        elif choice == "4":
            search_data(data)
        elif choice == "5":
            calculate_weekly_cost(data)
        elif choice == "0":
            print("Програма завершена")
            break
        else:
            print("Некоректний вибір. Спробуйте ще раз (0-5)")
main_menu()