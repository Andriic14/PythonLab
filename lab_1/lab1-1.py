a=int(input("Введіть додатне a:"))
while a < 0:
    a=int(input("Помилка, введіть додатне а:"))
b=int(input("Введіть додатне b:"))
while b < 0:
    b=int(input("Помилка, введіть додатне b:"))

if a>b:
    x=a*b-1
elif a==b:
    x=255
else:
    x = (a - 5) / b
print("Результат обчислення х: ", x)
