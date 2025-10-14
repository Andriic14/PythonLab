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
def calculator_total_cost(cars, min_power=100):
    total_cost = 0
    print(f"\nАвтомобілі з потужністю > {min_power} к.с.")
    for car_name, data  in cars.items():
        power = data[0]
        cost = data[1]

        if power > min_power:
            print(f"{car_name}: {power} к.с., {cost}")
            total_cost += cost
    print(f"Загальна вартість:{total_cost}")
    return total_cost
calculator_total_cost(cars)