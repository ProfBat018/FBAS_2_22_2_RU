# <editor-fold desc="Print keyword">

# print - Функция, которая выводит информацию в консоль
# ctrl + / Коментирует код и разкоментирует код

# print("Hello World")

# print("Hello")
# print("World")

# print("Hello"
#       "World")

# print(1, 2, 3, 4, 5)
# print("1", "2", "3", "4", "5")

# print("'Hello'")
# print('"Hello"')


# </editor-fold>

# <editor-fold desc="Escape sequences">

# print("\"Hello\"")
# print('\'Hello\'')

# print("Hello\nWorld")   # \n - newline
# print("Hello\tWorld")   # \t - tabulation, 4 spaces

# print("Hello\\\\World")

# print(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, sep=" ")  # sep - separate. Default value - Space

# print("Hello", end=" ")  # end - endline. Default value - \n
# print("World")

# </editor-fold>

# <editor-fold desc="Variables and data types">

# <editor-fold desc="Part 1">
# num1 and num2 = variables(переменная)
# Переменная - именновая область оперативной памяти, которая хранит в себе данные

# num1 = 5
# num2 = 6
#
# print(num1 + num2)

# </editor-fold>

# <editor-fold desc="Part 2. Naming cases">

# firstName = "Elvin"
# lastName = "Azimov"

# Camel Case - myFirstName
#   UpperCamelCase is the same as PascalCase
#   LowerCamelCase is simple camel case
# Pascal Case - MyFirstName
# Snake Case - Main variable naming case in Python. Example: first_name
# PascalSnake Case - First_Name
# kebab cased - my-first-name.

# </editor-fold>

# </editor-fold>

# <editor-fold desc="Data types">

# int - integer. Example: all negative and positive integer values, including zero.
# float - floating point number. Example: 3.25
# bool - Logical data type. Boolean. Can contain only True(1) or False(0). Everything except zero is True
# str(string) - Text data type in unicode encoding. Literals are "" and ''

# </editor-fold>

# <editor-fold desc="Input">

# Input - command for input. Default data type of input is STRING.

# num1 = int(input("Enter your number: "))  # 5
# num2 = int(input("Enter your number: "))  # 6
#
# result = num1 + num2
#
# print(num1, "+", num2, "=", result)
# print(f"{num1} + {num2} = {result}")     # string interpolation
# print("{} + {} = {}" .format(num1, num2, result))   # old version of interpolation
#
# </editor-fold>

# <editor-fold desc="Operators">

# Arithmetic - (+, -, *, /, %, **, //)
# Logical - (>, <, >=, <=, ==, !=)

# num1 = 5
# num2 = 2
#
# print(num1 + num2)  # 7 Сложение
# print(num1 - num2)  # 3 Вычитание
# print(num1 * num2)  # 10 Умножение
# print(num1 / num2)  # 2.5 Деление
# print(num1 ** num2)  # 25 Степень
# print(num1 // num2)  # 2 Целая часть от деления
# print(num1 % num2)  # 1 Остаток от деления


num1 = 5
num2 = 2

print(num1 > num2)
print(num1 < num2)
print(num1 >= num2)
print(num1 <= num2)
print(num1 == num2)
print(num1 != num2)

# </editor-fold>