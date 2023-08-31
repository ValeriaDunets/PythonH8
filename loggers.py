#для считывания данных и команд

def find_data():
    print("Введите название файла: ")
    name_file = input()
    data = open(name_file + '.txt', 'r', encoding='utf-8')
    for line in data:
        print(line)
    data.close()
#find_data()


def new_data():
    print("Введите название нового файла: ")
    new_file_name = input()
    data = open(new_file_name + '.txt', 'w', encoding='utf-8')
    print("Введите ФИО и номер телефона(+7) через пробел: ")
    original_data = input()
    data.write(original_data)
    data.close()
#new_data()

def correct_data():
    print("Введите имя файла, который нужно отредактировать: ")
    file_name = input()
    data = open(file_name + '.txt', 'r', encoding='utf-8')
    print(data.read())
    data.close()


    data = open(file_name + '.txt', 'w', encoding='utf-8')
    print("Введите новые данные через пробел: ")
    orig_data = input()
    data.write(orig_data)
    data.close()
#correct_data()


#Задача 38: Дополнить телефонный справочник возможностью изменения 
# и удаления данных. 
# Пользователь также может ввести имя или фамилию, 
# и Вы должны реализовать функционал для изменения и удаления данных


def delete_data():
    print("Введите имя файла, который нужно удалить: ")
    del_file = input()
    data = open(del_file + '.txt', 'r+', encoding='utf-8')
    import os
    os.remove("data04.txt")

#delete_data()

def correction_data():
    correction_data = input("Введите имя файла для изменения: ")
    data = open(correction_data + '.txt', 'r', encoding='utf-8')
    print(data.read())
    print("Какой параметр вы хотите изменить?: ")
    print('1 - ФИО\n'
          '2 - Номер телефона\n')
    file = int(input("Введите номер параметра: "))
    phone_book = " ".join(data)
    edit_phone_book = phone_book(file)
    elem = " ".join(edit_phone_book)
    first_name = input("Введите ФИО: ")
    phone = input("Введите номер телефона: ")
    num = elem[0]
    if len(first_name) == 0:
        first_name = elem[1]
    if len(phone) == 0:
        phone = elem[2]
    edited_line = f"{num} | {first_name} | {phone}"
    phone_book[file] = edited_line
    print("Запись изменена!")
    data = open(correction_data + '.txt', 'w', encoding='utf-8')
    data.write("\n".join(phone_book))
