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

def correction_data():
    correction_data = input("Введите имя файла для изменения: ")
    data = open(correction_data + '.txt', 'r', encoding='utf-8')
    print(data.read())
    print("Какой параметр вы хотите изменить?: ")
    print('1 - Фамилия\n'
          '2 - Имя\n'
          '3 - Отчество\n'
          '4 - Номер телефона\n')
    file = int(input("Введите номер параметра: "))
    if file == 1:
        print("Введите новую Фамилию: ")
        orig_data = input()
        data.split()
        data.writelines(orig_data)
        data.close()
    if file == 2:
        print("Введите новое Имя: ")
        orig_data = input()
        data.split()
        data.writelines(orig_data)
        data.close()
    else:
        print("Введите новый телефон: ")
        orig_data = input()
        data.split()
        data.writelines(orig_data)
        data.close()
correction_data()


def delete_data():
    print("Введите имя файла, который нужно удалить: ")
    del_file = input()
    data = open(del_file + '.txt', 'r+', encoding='utf-8')
    import os
    path = del_file
    os.remove(path)
    print("Файл удален")
    data.close()
#delete_data()


