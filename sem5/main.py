# Задача №31. Решение в группах
# Последовательностью Фибоначчи называется
# последовательность чисел a0, a1, ..., an, ..., где
# a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи
# Input: 7
# Output: 21
# Задание необходимо решать через рекурсию

# def fib(n):
#     if n in [1, 2]:
#         return 1
#     return fib(n-1) + fib(n-2)


# t = 7
# print(fib(t))
# list_1 = []
# for i in range(1, t+1):
#     list_1.append(fib(i))
# print(list_1)

# Поиск факториала числа через рекурсию

# def fact(n):
#     if n <= 1:
#         return n
#     else:
#         # print(n*fact(n-1))

#         return n*fact(n-1)


# print(fact(int(input("введите число "))))

# проверка на полиндром

# def poli(word):
#     if len(word) <= 1:
#         return 1
#     if word[0] == word[-1]:
#         return poli(word[1:-1])
#     else:
#         return 0
# print(poli("розаазор"))

# Задача №35. Решение в группах
# Напишите функцию, которая принимает одно число и
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое
# имеет 2 делителя: 1  и n(само число)
# решить через рекурсию
# Input: 5
# Output: yes

# def proverka(num, i=2):
#     if num == 1:
#         return "1"
#     if num == i:
#         return "yes"
#     if num % i == 0:
#         return "no"
#     return proverka(num, i+1)


# num = int(input("Введите число: "))
# print(proverka(num))


# Задача №37. Решение в группах
# Дано натуральное число N и
# последовательность из N элементов.
# Требуется вывести эту последовательность в
# обратном порядке.
# Примечание. В программе запрещается
# объявлять массивы и использовать циклы
# (даже для ввода и вывода).

# Input:    2 -> 3 4
# Output: 4 3
# def print_reverse(el):
#     if len(el) > 1:
#         print_reverse(el[1:])
#     print(el[0], end=" ")


# n = int(input("Введите количество элементов: "))
# print("введите числа через пробел")
# el = input().split()
# print_reverse(el)
def f(n):
    if n == 0:
        return '!'
    k = int(input())
    return f(n-1)+f' {k}'


n = int(input())
print(f(n))
