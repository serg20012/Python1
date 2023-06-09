# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии.
# *Пример:*
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 

# def stepen(a, b):
#     if b == 0:
#         return 1
#     else:
#         return a*stepen (a, b-1)
    
# a = int(input("Введите число: a "))
# b = int(input("Введите число: b "))
# print(stepen(a,b))


# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму 
# двух целых неотрицательных чисел. Из всех арифметических операций 
# допускаются только +1 и -1. Также нельзя использовать циклы.
# *Пример:*
# 2 2
#     4 
def sum(a, b, count=0):
    if a == 0:
        return b, count
    else:
        return sum(a - 1, b + 1, count + 1)


a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
if a > b:
    a,b = b,a
result, count = sum(a, b)
print("Сумма чисел:", result)
print("Количество рекурсивных вызовов:", count)
