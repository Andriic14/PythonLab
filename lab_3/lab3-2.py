num=input("Введіть чотиризначне число: ")

while len(num)!=4 or not num.isdigit():
    num=input("Введіть ще раз (має бути саме чотиризначне число): ")
count=num.count('7')
print("Цифра 7 зустрічається",count,"раз(и)")
