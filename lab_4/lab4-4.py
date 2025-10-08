def bubble_sort():
    A=list(map(int,input('Введіть елементи списку через пробіл: ').split()))
    print("\nОригінальний список:", A)
    if len(A)==0:
        print("Помилка! Список порожній")
        return None
    n=len(A)
    total_swaps = 0
    for i in range(n-1):
        print(f"\nПрохід {i + 1}")
        swaps=0
        for j in range(n-1-i):
            print(f"Порівнюємо А[{j}]={A[j]} і А[{j+1}]={A[j+1]}",end=" ")
            if A[j]>A[j+1]:
                A[j],A[j+1]=A[j+1],A[j]
                swaps+=1
                total_swaps+=1
                print(f"Міняємо тепер: {A}")
            else:
                print("Не міняємо")
        print(f"Список після проходу {i + 1}: {A}")
        print(f"Обмінів на цьому проході: {swaps}")
        if swaps==0:
            print("\nОбмінів не було, список відсортований")
            break
    print("Відсортований список:",A)
    print(f"Загальна кількість обмінів:{total_swaps}")
    return A
bubble_sort()