# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии.

def sqrt_function(a, b):
    if b == 0:
        return 1
    elif b == 1:
        return a
    else:
        b -= 1
        return a * sqrt_function(a, b)

a = int(input("Введите число: "))
b = int(input("Введите степень: "))
if b >= 0:
    result = sqrt_function(a, b)
else:
    c = b * -1
    result = 1 / sqrt_function(a, c) 
print(f"{a} ^ {b} = {result}")
