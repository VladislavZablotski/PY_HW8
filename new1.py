# with open("file.txt", "a", encoding="UTF-8") as f

# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. 
# Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
# Программа должна выводить данные
# Программа должна сохранять данные в текстовом файле
# Пользователь может ввести одну из характеристик для поиска определенной записи
# (Например имя или фамилию человека)
# Использование функций. Ваша программа не должна быть линейной

# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных. 
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал 
# для изменения и удаления данных

import os

filename = "tell.txt"

def load_tel():
    if os.path.isfile(filename):
        with open(filename, encoding="UTF-8") as f:
            r = f.readlines()
            s = []
            for line in r:
                s.append(line.split())
                
        return s
    s = []
   
    return s

def input_tel(s):
    first_name = input("Введите имя: ")
    patronimic = input("Введите отчество: ")
    last_name = input("Введите фамилию: ")
    tel = input("Введите номер телефона: ")
    with open(filename, "a", encoding="UTF-8") as f:
        f.write(f"{last_name} {first_name} {patronimic} {tel} \n")
    s.append([last_name, first_name, patronimic, tel])
    
    return s

def search_tel(s, object):
    for line in s:
        if object in line or object.capitalize() in line:
            return line
    return "Записи не найдено"

def show_tell(s):
    for line in s:
        print(" ".join(line))

def modify_data(r, object):
    remove_data(r, object)
    input_tel(r)
    return
            
def remove_data(r, object):
    if object in r:
            r.pop(r.index(object))
    with open(filename, "w", encoding="UTF-8") as f:
        for line in r:
            f.write(f"{' '.join(line)} \n")
        


if __name__ == "__main__":
    s = load_tel()
    while True:
        action = input("1 - Добавить данные \n2 - Искать данные \n3 - Посмотреть \n4 - Выход:\n")
        if action == "1":
            s = input_tel(s)
        elif action == "2":
            search_name = input("Текст для поиска:")
            result = search_tel(s, search_name)
            print(" ".join(result))
            if result != "Записи не найдено":
                datamod = input("1 - Изменить запись \n2 - Удалить запись \n3 - Выход в начальное меню:\n")
                if datamod == "1":
                    modify_data(s, result)
                    s = load_tel()
                elif datamod == "2":
                    remove_data(s, result)
                    s = load_tel()
                elif datamod == "3":
                    continue
                else:
                    print("Неверный выбор!")
                    continue
        elif action == "3":
            show_tell(s)
        elif action == "4":
            print("Good bye!")
            break
        else:
            print("Подумай!!!")