cars={
    "Toyota Camry":[150,25000],
    "Honda Civic": [90, 18000],
    "BMW X5": [250, 55000],
    "Ford Focus": [85, 15000],
    "Mercedes C-Class": [180, 45000],
    "Mazda 3": [95, 20000],
    "Audi A6": [200, 50000],
    "Volkswagen Polo": [75, 12000],
    "Lexus ES": [160, 40000],
    "Hyundai Elantra": [105, 19000]
}
def print_all_cars(cars):
    if not cars:
        print("\nСловник порожній")
        return
    print("ВСІ АВТОМОБІЛI")
    for car_name, data in cars.items():
        power,cost=data[0],data[1]
        print(f"Автомобіль  {car_name} - [{power}, {cost}]")
def add_car(cars):
    print("\nДОДАВАННЯ АВТОМОБІЛЯ")
    try:
        car_name=input("Введіть назву автомобіля: ").strip()
        if not car_name:
            print("Назва не може бути порожньою")
            return
        if car_name in cars:
            print(f"Автомобіль '{car_name}' вже існує")
            return
        power=int(input("Введіть потужність (к.с.): "))
        cost=int(input("Введіть вартість: "))
        if power<=0 or cost<=0:
            print("Потужність та вартість повинні бути додатними")
            return
        cars[car_name]=[power,cost]
        print(f"Додано автомобіль '{car_name}'")
    except ValueError:
        print("Помилка. Введіть числові значення для потужності та вартості.")
def delete_car(cars):
    print("\nВИДАЛЕННЯ АВТОМОБІЛЯ")
    if not cars:
        print("Словник порожній")
        return
    car_name=input("Введіть назву автомобіля для видалення: ").strip()
    try:
        if car_name in cars:
            del cars[car_name]
            print(f"Видалено автомобіль '{car_name}'")
        else:
            print(f"Автомобіль '{car_name}' не знайдено у словнику")
    except Exception as e:
        print(f"Помилка: {e}")

def print_sorted_cars(cars):
    if not cars:
        print("\nСловник порожній")
        return
    print("Відсортований словник (за алфавітом)")

    sorted_keys=sorted(cars.keys())
    for car_name in sorted_keys:
        power,cost=cars[car_name][0],cars[car_name][1]
        print(f"Автомобіль {car_name} - [{power}, {cost}]")

def calculator_total_cost(cars):
    if not cars:
        print("\nСловник порожній")
        return
    try:
        min_power=int(input("\nВведіть мінімальну потужність (к.с., за замовчуванням 100): ")or 100)
    except ValueError:
        print("Невірне значення! Використовую 100 к.с.")
        min_power = 100
    total_cost = 0
    count = 0
    print(f"\nАвтомобілі з потужністю > {min_power} к.с.")
    for car_name,(power,cost) in cars.items():
        if power > min_power:
            count += 1
            print(f"{car_name}: {power} к.с., {cost}")
            total_cost += cost
    if count == 0:
        print(f"Не знайдено автомобілів з потужністю >{min_power}")
    else:
        print(f"Знайдено автомобілів: {count}")
        print(f"Загальна вартість:{total_cost}")
    return total_cost
def show_menu():
    print("Меню роботи із словником")
    print("1 - Вивести всі значення словника")
    print("2 - Додати новий запис до словника")
    print("3 - Видалити запис зі словника")
    print("4 - Перегляд словника за відсортованими ключами")
    print("5 - Розрахунок загальної вартості (потужність > 100 к.с.)")
    print("0 - Вихід з програми")

def main():
    while True:
        show_menu()
        try:
            choice=input("Введіть пункт меню: ").strip()
            match choice:
                case "1":
                    print_all_cars(cars)
                case "2":
                    add_car(cars)
                case "3":
                    delete_car(cars)
                case "4":
                    print_sorted_cars(cars)
                case "5":
                    calculator_total_cost(cars)
                case "0":
                    break
                case _:
                    print(f"Невірний вибір: {choice}. Спробуйте ще раз.")
        except KeyboardInterrupt:
            break
main()
