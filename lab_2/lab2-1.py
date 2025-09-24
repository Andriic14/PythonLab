import math
from mod import product

def expression (x):
    if x < 0 or x >= 1:
        print("Помилка: для обчислення потрібно, щоб 0 ≤ x < 1")
        return None
    z=math.exp(math.sqrt(x))/math.sqrt(1-x)
    return z


x = float(input("Введіть значення x: "))
print("Значення виразу z =", expression(x))
N = int(input("Введіть значення N: "))
print("Значення добутку =", product(N))