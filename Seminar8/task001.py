# Задача №55. Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. 
# Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
# Программа должна выводить данные
# Программа должна сохранять данные в текстовом файле
# Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
# Использование функций. Ваша программа не должна быть линейной

# 1. Создание файла
# 2. Добавление новой записи:
#     - забрать ввод пользователя
#     - открыть файл
#     - записать в файл
# 3. Вывод на экран
#     - открыть файл на чтение
#     - считать данные
#     - вывод на экран
# 4. Поиск контакта
#     - выбрать вариант поиска
#     - забрать ввод пользователя
#     - открытие файла на чтение
#     - считать данные
#     - осуществить поиск
#     - вывести результат поиска
# 5. Создание интерфейса

def name_input():
    return input('Введите имя: ').title()

def suname_input():
    return input('Введите фамилию: ').title()

def patronymic_input():
    return input('Введите отчество: ').title()

def phone_input():
    return input('Введите номер: ')

def address_input():
    return input('Введите адрес: ').title()




def create_contact():
    
        suname = suname_input()
        name = name_input()
        patronymic = patronymic_input()
        phone = phone_input()
        address = address_input()
        return f'{suname} {name} {patronymic} {phone}\n{address}\n\n'

def write_contact():
    contact = create_contact()
    with open('phonebook.txt', 'a', encoding='utf-8') as file:
        file.write(contact)
        print('\nКонтакт записан\n')


def print_contacts():
    # with open('phonebook.txt', 'r', encoding='utf-8') as file:
    #     print()
    #     print(file.read())
    #     print()
    # 2
    with open('phonebook.txt', 'r', encoding='utf-8') as file:
        contacts_list = file.read().rstrip().split('\n\n')
        for nn, contact in enumerate(contacts_list, 1):
            print(f'{nn}. {contact}\n')

            

def search_contact():
    print(
        'Возможные варианты поиска:\n'
        '1. По фамилии\n'
        '2. По имени\n'
        '3. По отчеству\n'
        '4. По номеру\n'
        '5. По городу\n'
        )
    
    index_var = int(input('Введите вариант поиска: ')) - 1

    search = input('Введите данные поиска: ')

    with open('phonebook.txt', 'r', encoding='utf-8') as file:
        contacts_str = file.read()

    # print({data_str})
    contacts_list = contacts_str.rstrip().split('\n\n')
    # print(contacts_list)
    for contact_str in contacts_list:
        contact_list = contact_str.replace('\n', ' ').split(' ')
        if search in contact_list[index_var]:
            print(f'\n{contact_str}\n')
            
def copy_contacts():
    print_contacts()
    with open('phonebook.txt', 'r', encoding='utf-8') as file:
        contacts_list = file.read().rstrip().split('\n\n')
    number_contact = int(input('Выберите номер контакта: '))
    while number_contact < 1 or number_contact > len(contacts_list):
        print('Некорректный ввод')
        number_contact = int(input('Выберите номер контакта: '))
        
    with open('copy_phonbook.txt', 'a', encoding='utf-8') as file:
        file.write(f'{contacts_list[number_contact - 1]}\n')
        print(f'\nКонтакт скопирован\n')



def interface():
    with open('phonebook.txt', 'a'):
        pass
    
    user_input = None
    while user_input != '5':
        print(
            'Возможные варианты действия:\n'
            '1. Добавить контакт\n'
            '2. Вывод списка контактов\n'
            '3. Поиск контакта\n'
            '4. Копировать контакт\n'
            '5. Выход из программы\n'
            
            )
    
        user_input = input('Введите вариант: ')
        while user_input not in ('1', '2', '3', '4', '5'):
            print('Некорректный ввод')
            user_input = input('Введите вариант: ')

        print()

        match user_input:
            case '1':
                write_contact()
            case '2':
                print_contacts()
            case '3':
                search_contact()
            case '4':
                copy_contacts()
        print()
    

if __name__ == '__main__':
    interface()