# 3. Пользователь вводит с клавиатуры строку, слово для поиска, слово для замены.
# Произведите в строке замену одного слова на другое. Полученную строку отобразите на экране.
# Предположим, что можно вводить и числа, и спец символы, а замена будет происходить только 1 раз.

try:
    user_string = input("Enter your string: ")
    user_change = input("Enter word to find: ")

    if user_change in user_string:
        print("Find word to change")
        user_replace = input("Enter word to replace: ")
        user_string = user_string.replace(user_change, user_replace, 1)
        print(f"New string: {user_string}")
    else:
        print("No such word in the string")

except Exception as error:
    print(error)



