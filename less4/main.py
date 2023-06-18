# def f(x):
#     return x*x

# print(f(5))
# print(type(f))
# a = f
# print(type(a))
# print(a(5))
# def calk1(a):
# #     return a+a
# def calk2(a):
#     return a*a
# def math(op, x):
#     print(op(x))
# math(calk1, 5)
# def calk1(a, b): return a+b


# print(calk1(5, 10))
# data = [1, 2, 3, 5, 8, 15, 23, 38]
# list_1 = [(i, i**2) for i in data if i % 2 == 0]
# print(*list_1)

list_1 = [x for x in range(1, 20)]
print(*list_1)
list_1 = map(lambda x: x+10, list_1)
print(*list_1)

# Задача: C клавиатуры вводится некий набор чисел, в качестве разделителя
# используется пробел. Этот набор чисел будет считан в качестве строки. Как
# превратить list строк в list чисел?

# 1. Маленькое отступление, функция строка.split() - убирает все пробелы и создаем
# список из значений строки, пример:
# data = '1 2 3 5 8 15 23 38'.split()
# print(data) # ['1', '2', '3', '5', '8', '15', '23', '38']
# data = "15 156 96 3 5 8 52 5"
# print(data)
# data1 = data.split()
# print(data1)
# data2 = list(map(int, data1))
# print(data2)

# data = [x for x in range(10)]
# res = list(filter(lambda x: x % 2 == 0, data))
# print(res)  # [0, 2, 4, 6, 8]

# users = ['user1', 'user2', 'user3', 'user4', 'user5']
# ids = [4, 5, 9, 14, 7]
# data = list(zip(users, ids))
# # [('user1', 4), ('user2', 5), ('user3', 9), ('user4', 14),\
# # ('user5', 7)]
# print(*data)

# users = ['user1', 'user2', 'user3']
# data = list(enumerate(users))
# print(data)  # [(0, 'user1'), (1, 'user2'), (2, 'user3))]

# colors = ['red', '89+8', 'blue']
# # здесь указываем режим, в котором будем работать
# data = open('file.txt', 'a')
# data.writelines(colors)  # разделителей не будет
# data.close()

# with open('file.txt', 'w') as data:
#     data.write('line 1\n')
#     data.write('line 3\n')

# path = 'file.txt'
# data = open(path, 'r')
# for line in data:
#     print(line)
# data.close()
