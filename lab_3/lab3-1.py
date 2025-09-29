text=str(input("Введіть будь-який рядок: "))
while (len(text) < 7):
    text=str(input("Введіть ще раз рядок, рядок занадто короткий, : "))
else:
    print("Кожний 7-й символ:", text[6::7])
