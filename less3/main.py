# def sum_numbers(n, y="Hello"):
#     print(y)
#     summa = 0
#     for i in range(1, n+1):
#         summa += i
#     print(n)
#     return summa
# a = sum_numbers(5, "dfs")
# print(a)

# def sum_str(*args):
#     res = ""
#     for i in args:
#         res += i
#     return res

# print(sum_str('q', 'e', 'l'))
# print(sum_str('q', 'e', 'l', 'w'))
# print(sum_str('1', '8', '9'))

# import modul1
# print(modul1.max1(55, 565))

# def fib(n):
#     if n in [1, 2]:
#         return 1
#     return fib(n-1) + fib(n-2)


# list_1 = []
# for i in range(1, 10):
#     list_1.append(fib(i))
# print(list_1)

# def sortq(array):
#     if len(array) <= 1:
#         return array
#     else:
#         pivot = array[0]
#     less = [i for i in array[1:] if i <= pivot]
#     greater = [i for i in array[1:] if i > pivot]
#     return sortq(less) + [pivot] + sortq(greater)


# print(sortq([10, 5, 2]))
