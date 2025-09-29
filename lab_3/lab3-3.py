sentence =str(input("Введіть речення: "))
words=sentence.split()
result=[word for word in words if word.lower().startswith('к')]
if result:
    print("Слово, що починається на 'к':", ", ".join(result))
else:
    print("Немає слів, що починаються на 'к'")