# <editor-fold desc="Linear">

# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
#
# addition = num1 + num2
# subtraction = num1 - num2
# multiplication = num1 * num2
# division = num1 / num2
# integer_div = num1 // num2
# remain_div = num1 % num2
# power = num1 ** num2
#
# print(f"{num1} + {num2} = {addition}")
# print(f"{num1} - {num2} = {subtraction}")
# print(f"{num1} * {num2} = {multiplication}")
# print(f"{num1} / {num2} = {division}")
# print(f"{num1} // {num2} = {integer_div}")
# print(f"{num1} % {num2} = {remain_div}")
# print(f"{num1} ** {num2} = {power}")

# </editor-fold>

# <editor-fold desc="If part 1">

# num1 = 6
# num2 = 5
#
# print("Before If")
# if num1 > num2:     # Любое условие, возвращает либо True, либо False
#     print("If Started")
#     print(num1, '>', num2)
#     print("If ended")
# print("After if")

# </editor-fold>

# <editor-fold desc="If Part 2">

# result = 5 + 1
#
# if not(not result):
#     print("Hello World")

# </editor-fold>

# <editor-fold desc="Else">

# num1 = 5
# num2 = 5
#
# if num1 > num2:
#     print(f"{num1} > {num2}")
# if num1 < num2:
#     print(f"{num1} < {num2}")
# else:
#     print(f"{num1} = {num2}")


# </editor-fold>

# <editor-fold desc="Else 2">

# num1 = 6
# num2 = 2
#
# if num1 > num2:
#     print(f"{num1} > {num2}")
# if num1 % num2 == 0:
#     print(f"{num1} % {num2}")
# if num1 == num2:
#     print(f"{num1} == {num2}")
# if num2 % num1:
#     print(f"{num2} % {num1}")
# else:
#     print("This is else...🐱‍🐱🐱‍")

# </editor-fold>

# <editor-fold desc="Region">
import time

num1 = 2
num2 = 6

if num1 > num2:
    print(f"{num1} > {num2}")
else:
    if num1 % num2 == 0:
        print(f"{num1} % {num2}")
    else:
        if num1 == num2:
            print(f"{num1} == {num2}")
        else:
            if num2 % num1:
                print(f"{num2} % {num1}")
            else:
                print("This is else...🐱‍🐱🐱‍")


# if num1 > num2:
#     print(f"{num1} > {num2}")
# elif num1 % num2 == 0:      # else if
#     print(f"{num1} % {num2}")
# elif num1 == num2:
#     print(f"{num1} == {num2}")
# elif num2 % num1:
#     print(f"{num2} % {num1}")
# else:
#     print("This is else...🐱‍🐱🐱‍")

# </editor-fold>


num = int(input("Enter your number: "))

n1 = num % 10
n2 = (num // 10) % 10
n3 = (num // 100) % 10

print(n1)
print(n2)
print(n3)
print(n1 + n2 + n3)


time.sleep(5000)