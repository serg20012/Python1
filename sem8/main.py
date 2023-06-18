# Задача №49. Общее обсуждение Создать телефонный справочник с 
# возможностью импорта и экспорта данных в формате .txt. Фамилия, имя, отчество, 
# номер телефона - данные, которые должны находиться в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для 
# поиска определенной записи(Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной

# Задача 38: Дополнить телефонный справочник возможностью
# изменения и удаления данных. Пользователь также может ввести
# имя или фамилию, и Вы должны реализовать функционал для 
# изменения и удаления данных

choice =0
def read_file():
    path = r'C:\Users\Dom-1floor\Documents\GB\Python\sem8\phon.txt'
    data = [] 
    fields = ["Фамилия", "Имя", "телефон", "описание"]
    with open(path, 'r', encoding='utf-8') as fin:
        for line in fin:
            record = dict(zip(fields, line.strip().split(",")))
            data.append(record)
    return data

def save_data(data):
    path = r'C:\Users\Dom-1floor\Documents\GB\Python\sem8\phon.txt'
    with open(path, 'w', encoding='utf-8') as fout:
        for record in data:
            line = ','.join(record.values()) + '\n'
            fout.write(line)

data = read_file()

def search_fam():
    fam = input("введите Фамилию ")
    for i in data:
        if i["Фамилия"] == fam : print (i) 
    else: print("Контакт не найден")

def edit_contact():
    fam = input("введите Фамилию контакта для редактирования ")
    fields = ["Фамилия", "Имя", "телефон", "описание"]
    for i in data:
        if i["Фамилия"] == fam:
            new_data = input ("Ведите через запятую новые данные контакта ")
            new_data = new_data.split(",")
            if len(new_data) == 4:
                for a, b in enumerate(fields):
                    i[b] = new_data[a]
                print("Контакт отредактирован")            
                save_data(data)
                return
            else: print ("невернный ввод")
    else: print("Контакт не найден")
def print_book():
    for i in data:
        print (i)
        
def del_contact():
    fam = input("введите Фамилию контакта для удаления ")
    for i in data:
        if i["Фамилия"] == fam:
            data.remove(i)
            print("Контакт удален")            
            save_data(data)
            return
    else: print("Контакт не найден")

def new_contact():
    fields = ["Фамилия", "Имя", "телефон", "описание"]
    new_data = input ("Ведите через запятую новый контакта ")
    new_data = new_data.split(",")
    if len(new_data) == 4:
        contact = dict(zip(fields, new_data))
        print("Контакт создан")
        data.append(contact)
        save_data(data)
        return
    else: print ("невернный ввод")
    
while choice != 6:
    choice = int(input("Выберите действие со справочником: "
                       "(вывод по Фамилии = 1, редактирование контакта = 2, "
                       "вывод всего = 3, удаление контакта = 4,"
                        "новый контакт = 5 выход = 6: "))
    if choice ==1:
        search_fam()
    elif choice ==2:
        edit_contact()
    elif choice ==3:
        print_book()
    elif choice ==4:
        del_contact()
    elif choice ==5:
        new_contact()
    elif choice ==6:
        break