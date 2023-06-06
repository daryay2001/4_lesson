# 2. Пользователь вводит с клавиатуры строку и символ для поиска.
# Посчитайте сколько раз в строке встречается искомый символ.
# Полученное число выведите на экран.

# sym_num = 0
#
# try:
#     user_string = input("Enter your string: ")
#     sym = input("Enter symbol to find: ")
#
#     if len(sym) > 1:
#         raise Exception("Please, enter just 1 symbol to find!")
#
#     for i in user_string:
#         if i == sym:
#             sym_num += 1
#
#     print(f"{sym_num} symbols")
#
# except Exception as error:
#     print(error)