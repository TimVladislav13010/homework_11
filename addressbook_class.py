from collections import UserDict


"""
Класи бота помічника.

Record
AddressBook(UserDict)
Field
Name(Field)
Phone(Field)
"""


class Record:
    """
    Клас Record, який відповідає за логіку додавання/видалення/редагування необов'язкових полів та зберігання
    обов'язкового поля Name.

    При ініціалізації класу створюється ім'я класу Name, та список номерів телефоні, в який будуть записані номери
    телефонів класу Phone.
    """
    def __init__(self, name: str):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phones):
        self.phones.append(Phone(phones))

    def return_record(self):

        phone_numbers = ""
        for phone in self.phones:
            phone_numbers += f"{phone.value}, "
        return f"{self.name.value}: {phone_numbers[:-2]}"

    def change_phone_record(self, new_phone):
        """
        Метод для зміни номера телефона в існуючого контакту.

        1. Якщо в існуючого контакту немає номерів він додає номер телефону до списку класу Phone.
        2. Якщо номер один в списку то він замінюється на new_phone.
        3. Якщо номерів декілька в списку контакта замінити на той що вибере користувач за індексом.
        :param new_phone:
        :return:
        """
        if len(self.phones) == 0:
            self.phones.append(Phone(new_phone))

        if len(self.phones) == 1:
            self.phones[0].change_value(new_phone)

        if len(self.phones) > 1:
            i = -1
            print(f"Виберіть номер телефону для видалення")
            for phone in self.phones:
                i += 1
                print(f"№  {i}  :  {phone.value}")
            inp_user = int(input(f"Введіть №..."))
            self.phones[inp_user] = Phone(new_phone)

    def delete_phone_record(self, name):
        """
        Метод для видалення номеру в існуючого контакту.

        1. Якщо в існуючого контакту немає номерів повернення строки.
        2. Якщо номер один в списку то він видаляється.
        3. Якщо номерів декілька в списку контакта видаляється той що вибере користувач за індексом.
        :param name:
        :return:
        """
        if len(self.phones) == 0:
            return f"У контакта немає номерів..."

        elif len(self.phones) == 1:
            number = self.phones[0].return_value()
            self.phones.pop(0)
            return f"{number}"

        elif len(self.phones) > 1:
            i = -1
            print(f"Виберіть номер телефону для видалення")
            for phone in self.phones:
                i += 1
                print(f"№  {i}  :  {phone.value}")
            inp_user = int(input(f"Введіть №..."))
            number = self.phones[inp_user].return_value()
            self.phones.pop(inp_user)
            return f"{number}"


class AddressBook(UserDict):
    """
    Клас книги контактів.

    Батьківський клас UserDict.
    """
    def add_record(self, record):
        self.data[record.name.value] = record

    def get_records(self):
        return self.data

    def get_name_record(self, name) -> Record:
        return self.data.get(name)


class Field:
    """
    Батьківський клас для Name, Phone.
    """
    def __init__(self, value):
        self.value = value

    def change_value(self, new_value):
        """
        Метод для зміни значення value.
        :param new_value:
        :return:
        """
        self.value = new_value

    def return_value(self):
        return self.value


class Name(Field):
    """
    Ім'я контакта.
    """
    pass


class Phone(Field):
    """
    Номер телефону контакта.

    Додається до списку phones, який створюється при ініціалізації класу Record.
    """
    pass
