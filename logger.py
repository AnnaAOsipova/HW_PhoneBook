from data_create import name_data, surname_data, phone_data, adress_data

def input_data():
    name = name_data()  # эту функцию создадим в другом файле, откуда будем брать эту инфу
    surname = surname_data()
    phone = phone_data()
    adress = adress_data()
    var = int(input(f"В каком формате записать данные\n\n"
    f"1 вариант: \n"
    f"{name}\n{surname}\n{phone}\n{adress}\n\n"
    f"2 вариант: \n"
    f"{name}; {surname}; {phone}; {adress}\n"
    f"Выберите вариант: "))

    while var != 1 and var != 2:  # если введено не число 1 или 2, просим пользователя повторить ввод
        print("Неправильный ввод")
        var = int(input('Введите число '))

    if var == 1:
        with open('Data_first.csv', 'a', encoding = 'utf-8') as f:
            f.write(f"{name}\n{surname}\n{phone}\n{adress}\n\n")

    elif var == 2:
        with open('Data_second.csv', 'a', encoding = 'utf-8') as f:
            f.write(f"{name}; {surname}; {phone}; {adress}\n")
    return var # Для дальнейшей работы с change_data


def change_data():  # Изменяет информацию из файла
    n = int(input('Введите номер записи, которую хотите изменить '))
    m = input_data() # Вызываем функцию для записи новых данных в конец файла
    if m == 1:
        with open('Data_first.csv','r', encoding = 'utf-8') as f:
            data_first = f.readlines()
        data_first_list = [] # создаем пустой список для сохранения элементов

        j = 0   
        for i in range (len(data_first)):
            if data_first[i] == '\n' and data_first[i] != '\n\n' or i == len(data_first) - 1: # проверяем что есть какая-то запись. 
                # Если iй элемент = переходу на новую строку или i = последней записи. Удаляем лишние переносы строк
                data_first_list.append(''.join(data_first[j:i+1])) # Объединяем data_first и с помощью среза от j до i+1 - добавляем запись от 0 до 1, потом от 1 до 2 и тд
                j = i
        print(''. join(data_first_list))

        data_first_list_1 = [] # создаем пустой список для формирования конечного результата с изменениями

        change_el = data_first_list.pop() # удаляем последний элемент из списка и записываем его в переменную change_el для последующей записи в выбранный номер элемента
        data_first_list_1 = data_first_list[:n-1] + [change_el] + data_first_list[n:] # записываем элементы до, измененный элемент и все после него
        
        with open('Data_first.csv','w', encoding = 'utf-8') as f:
            f.writelines(data_first_list_1)
       # print(data_first_list_1)
    elif m == 2:
        with open('Data_second.csv','r', encoding = 'utf-8') as f:
            data_second = f.readlines()
            change_el = data_second.pop()
            data_second_list = data_second[:n-1] + [change_el] + data_second[n:]
        with open('Data_second.csv','w', encoding = 'utf-8') as f:
            f.writelines(data_second_list)

# change_data()      

def delete_data():  # Удаляет информацию из файла
    var = int(input(f"В каком формате хотите удалить данные\n\n"
    f"1 вариант: \n"
    f"{'name'}\n{'surname'}\n{'phone'}\n{'adress'}\n\n"
    f"2 вариант: \n"
    f"{'name'}; {'surname'}; {'phone'}; {'adress'}\n"
    f"Выберите вариант: "))

    while var != 1 and var != 2:  # если введено не число 1 или 2, просим пользователя повторить ввод
        print("Неправильный ввод")
        var = int(input('Введите число '))
    n = int(input('Введите номер записи для удаления: '))

    if var == 1:
        with open('Data_first.csv', 'r', encoding = 'utf-8') as f:
            data_first = f.readlines()
            j = 0
            data_first_list = []
            for i in range(len(data_first)):
                  if data_first[i] == '\n' and data_first[i] != '\n\n' or i == len(data_first) - 1:
                    data_first_list.append(''.join(data_first[j:i+1])) 
                    j = i
            data_first_list_1 = data_first_list[:n-1] + data_first_list[n:] # Записываем новый список без удаляемого элемента
        with open('Data_first.csv', 'w', encoding = 'utf-8') as f:
            f.writelines(data_first_list_1)
    
    elif var == 2:
        with open('Data_second.csv','r', encoding = 'utf-8') as f:
            data_second = f.readlines()
            data_second_list = data_second[:n-1] + data_second[n:]
        with open('Data_second.csv','w', encoding = 'utf-8') as f:
            f.writelines(data_second_list)
# delete_data()

def print_data():
    print('Вывожу данные из 1 файла: \n')
    with open('Data_first.csv', 'r', encoding = 'utf-8') as f: # открываем файл для вывода данных, ставим режим чтения
        data_first = f.readlines()  # прочитали все наши строки
        data_first_list = []  # создаем список, в котором будет храниться итоговый результат
        j = 0   
        for i in range (len(data_first)):
            if data_first[i] == '\n' or i == len(data_first) - 1: 
                data_first_list.append(''.join(data_first[j:i+1])) 
                j = 1
        print(''. join(data_first_list)) # через join чтобы выводить в виде строки

    print('Вывожу данные из 2 файла: \n')
    with open('Data_second.csv', 'r', encoding = 'utf-8') as f:
        data_second = f.readlines()  # прочитали все наши строки
        print(*data_second)      # так как запись во втором варианте построчна, то просто выводим на печать, с распаковкой через *

# print_data()
