n = int(input("Введіть число N (1 < N < 9): "))
for i in range(n, 0, -1):
    spaces = " " * ((n*2)-2)
    print(spaces, end=" ")
    for j in range(i, n+1):
        print(j, end=" ")
    print("")
for i in range(1, n+1):
    spaces = " " * ((n - i)*2)
    print(spaces, end=" ")
    for j in range(i, 0, -1):
        print(j, end=" ")
    print("")