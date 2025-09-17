days=1
distance=10
totalDistance=10
print("День", " ", "Км за день", " ", "Загальна дистанція")
print(days, " " * 4, distance, " " * 9, totalDistance)

while totalDistance < 50:
    days += 1
    distance = round(distance * 1.1, 1)
    totalDistance = round(totalDistance + distance, 1)
    print(days, " " * 4, distance, " " * 7, totalDistance)
