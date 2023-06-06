# Задача №25. Решение в группах
# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию
# .split()
# text = "a a a b c a a d c d d"
# words = text.split()

# counter = {}
# result = []

# for word in words:
#     if word in counter:
#         counter[word] += 1
#         print(counter[word])
#         result.append(f"{word}_{counter[word]}")
#         print(result)
#     else:
#         counter[word] = 0
#         result.append(word)
#         print(result)

# output = " ".join(result)
# print(*result)
# print(output)

# Задача №27. Решение в группах
# Пользователь вводит текст(строка). Словом считается
# последовательность непробельных символов идущих
# подряд, слова разделены одним или большим числом
# пробелов. Определите, сколько различных слов
# содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells
# that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore I'm sure that the shells are sea
# shore shells
# Output: 13

# text = "She sells sea shells on the sea shore The shells "\
#     "that she sells are sea shells I'm sure.So if she sells sea "\
#     "shells on the sea shore I'm sure that the shells are sea "\
#     "shore shells"
# # text = text.upper()
# words = text.upper().split()
# unique_words = set(words)
# count = len(unique_words)
# print(unique_words)
# print("Количество различных слов в тексте:", count)


# задача  из чата записи
# Даны несколько телефонных номеров необходимо создать список с ключем код
# страны и значение телефонный номер. Код страны "+" и одна цифра
# решение из зала
# s = '+71234567890 +71234567892 +61234567890 +51234567890 '\
#     '+21234567890 +271234567891 +71234567893'.split()
# d = {}
# for i in s:
#     d[i[:2]] = [x for x in s if x[:2] == i[:2]]
# print(*sorted(d.items()))
# print(*sorted(d))
# print(*d.items())

# решение мое
# s = '+71234567890 +71234567892 +61234567890 +51234567890 +21234567890 '\
#     '+271234567891 +71234567893'
# numbers = s.split()
# phone_dict = {}

# for number in numbers:
#     # Получаем код страны (второй символ номера)
#     country_code = number[1]
#     if country_code in phone_dict:
#         # Добавляем номер в список значений по ключу кода страны
#         phone_dict[country_code].append(number)
#     else:
#         # Создаем новую запись в словаре с ключом кода страны и списком значений
#         phone_dict[country_code] = [number]

# print(phone_dict)
