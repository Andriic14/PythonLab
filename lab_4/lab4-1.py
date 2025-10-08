n=int(input("Введіть n= "))
if n<=0:
    print("Помилка. Кількість елементів має бути більше 0")
else:
    print(f"Введіть {n} елементів масиву")
    arr=[int(input()) for i in range(n)]
    print("\nОригінальний масив: ", arr)
product = 1
odd_indices_elements=[]
for i in range(n):
    if i % 2 != 0: # Перевірка чи індекс непарний
        product *= arr[i]
        odd_indices_elements.append(arr[i])
print("\nЕлементи з непарними індексами:", odd_indices_elements)
if odd_indices_elements:
    print(f"Добуток елементів з непарними індексами: {product}")
else:
    print("У масиві немає елементів з непарними індексами")