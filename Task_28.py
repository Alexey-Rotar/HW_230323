# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

def sum_function(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    elif a <= b:
        a -= 1
        b += 1
        return sum_function(a, b)
    else:
        b -= 1
        a += 1
        return sum_function(a, b)

a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))

print(f"{a} + {b} = {sum_function(a, b)}")
