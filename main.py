from addressbook_class import AddressBook, Record


"""
Бот помічник.
Працює з командами (help, hello, add, change, delete_user, user_add_phone, user_delete_phone, phone, show_all, 
good_bye, close, exit, .)
"""


PHONE_BOOK = AddressBook()


def input_error(func):
    """
    Обробник помилок
    """

    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except TypeError:
            return f"Wrong command."
        except KeyError:
            return f"KeyError"
        except IndexError:
            return f"Wrong index"
        except ValueError:
            return f"ValueError"

    return wrapper


@input_error
def change_input(user_input):
    """
    Функція для обробки введених даних від користувача
    """
    new_input = user_input
    data = ''
    for key in USER_COMMANDS:
        if user_input.strip().lower().startswith(key):
            new_input = key
            data = user_input[len(new_input)+1:]
            break
    if data:
        return handler(new_input)(data)
    return handler(new_input)()


def hello():
    return "How can I help you?"


@input_error
def add(data):
    """
    Функція для додавання нового номеру в телефонну книгу
    """
    name, phones = create_data(data)
    if name in PHONE_BOOK:
        return f"Цей контакт {name} вже використовується введіть інше ім`я"
    record = Record(name)
    record.add_phone(phones)
    PHONE_BOOK.add_record(record)
    return f"Запис ({name} : {phones}) успішно додано до словника"


@input_error
def create_data(data):
    """
    Розділяє вхідні дані - номер і телефон.
    """
    name, phones = data.strip().split(' ')

    if name.isnumeric():
        raise ValueError('Wrong name.')
    for phon in phones:
        if not phon.isnumeric():
            raise ValueError('Wrong phones.')
    return name.title(), phones


@input_error
def change(data):
    """
    Функціця для змінни існуючого номеру в телефонній книзі
    """
    name, number = data.strip().split(' ')
    name = name.title()
    if name not in PHONE_BOOK:
        return f"{name} імя не знайдено в словнику"

    elif not number.isdigit():
        return f"{number} не номер телефону будь ласка введіть числа"
    records = PHONE_BOOK[name]
    records.change_phone_record(number)
    return f"Запис ({name} : {number}) замінено в словнику"


def delete_user(name):
    """
    Функція видалення контакту.
    :param name:
    :return:
    """
    name = name.title()

    if name not in PHONE_BOOK:
        return f"{name} імя не знайдено в словнику"

    record = PHONE_BOOK.pop(name)
    return f"Запис ({record.return_record()}) видалено з словника."


@input_error
def user_add_phone(data):
    """
    Функціця для додавання номеру до існуючого контакту.
    """
    name, number = data.strip().split(' ')
    name = name.title()
    if name not in PHONE_BOOK:
        return f"{name} імя не знайдено в словнику"

    elif not number.isdigit():
        return f"{number} не номер телефону будь ласка введіть числа"
    record = PHONE_BOOK[name]
    record.add_phone(number)
    return f"Номер ({number}) додано до контакту {name}"


def user_delete_phone(name):
    """
    Функціця для видалення номеру в існуючого контакту.
    """
    name = name.title()
    if name not in PHONE_BOOK:
        return f"{name} імя не знайдено в словнику"
    record = PHONE_BOOK[name]
    result = record.delete_phone_record(name)
    returns = f"У контакта немає номерів..."
    if result in returns:
        return returns
    return f"Номер телефону: {result}, видалено в контакта {name}"


def phone(name):
    """
    Функція повертає номер телефону з телефонної книги
    """
    name = name.title().strip()
    if not PHONE_BOOK.get_name_record(name):
        return f"{name} не знайдено в телефонній книзі"
    phones = PHONE_BOOK.get_name_record(name).return_record()
    return f"Інфомацію знайдено:\n{phones}"


def show_all():
    """
    Функція для відображення всієї телефонної книги
    """
    show_number = ""
    for key, val in PHONE_BOOK.get_records().items():
        show_number += f"{val.return_record()}\n"
    return show_number


def good_bye():
    return "Good Bye!"


def break_f():
    """
    Коли користувач введе щось інше крім команд повертається строка про неправильний ввід команди.
    """
    return f"Wrong enter... "


@input_error
def handler(commands):
    return USER_COMMANDS.get(commands, break_f)


def helps():
    return f"Команди на які відповідає помічник: \n"\
           "help\n"\
           "hello \n"\
           "add - (add name phone)\n"\
           "delete_user - (delete_user name)\n"\
           "change - (change name phone)\n"\
           "phone - (phone name)\n"\
           "user_add_phone - (user_add_phone name phone)\n"\
           "user_delete_phone - (user_delete_phone name)\n"\
           "show_all\n"\
           "good_bye, close, exit, .\n"


USER_COMMANDS = {
    "hello": hello,
    "add": add,
    "change": change,
    "user_add_phone": user_add_phone,
    "user_delete_phone": user_delete_phone,
    "delete_user": delete_user,
    "phone": phone,
    "show_all": show_all,
    "good_bye": good_bye,
    "close": good_bye,
    "exit": good_bye,
    ".": good_bye,
    "help": helps
}


def main():
    """
    Логіка роботи бота помічника
    """
    while True:
        user_input = input("Введіть будь ласка команду: (або скористайтеся командою help)\n")
        result = change_input(user_input)
        print(result)
        if result == "Good Bye!":
            break


if __name__ == "__main__":
    main()
