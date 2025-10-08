def split_list():
    A= list(map(int, input('Введіть елементи списку через пробіл: ').split())) # Введення списку з клавіатури
    # Виведення оригінального списку
    print("\nОригінальний список:",A)
    print("Індекси:            ",list(range(len(A))))
    # Перевірка чи список не порожній
    if len(A) == 0:
        print("Помилка. Список порожній")
        return None, None

    k=int(input(f'\nВведіть індекс для розбиття (0-{len(A)}): '))# Введення індексу для розбиття
    # Перевірка коректності індексу
    if k<0 or k>len(A):
        print(f"Помилка! Індекс має бути в діапазоні від 0 до {len(A)}")
        return None, None
    # Розбиття списку на два списки
    list1=[]
    list2=[]
    for i in range(len(A)):
        if i<k:
            list1.append(A[i])
        else:
            list2.append(A[i])
    print(f"\nПерший список (індекси 0-{k-1}):", list1)
    print(f"Другий список (індекси {k}-{len(A)-1}):", list2)
    return list1, list2
split_list()