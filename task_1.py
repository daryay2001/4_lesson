# 1. Пользователь вводит с клавиатуры строку.
# Посчитайте количество букв, цифр в строке.
# Выведите оба количества на экран. (использовать цикл)

lett = 0
num = 0
try:
    user_string = input("Enter your string: ")
    for i in user_string:
        if i.isdigit():
            num += 1

        elif i.isalpha():
            lett += 1
    print(f"numbers: {num} letters: {lett}")
except Exception as error:
    print(error)

