import csv
import os


class InstantiateCSVError(Exception):
    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else "Файл item.csv поврежден"


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f"{self.__name}"

    def __add__(self, other):
        if issubclass(other.__class__, self.__class__):
            return self.quantity + other.quantity
        else:
            raise ValueError('Складывать можно только объекты Item и дочерние от них.')

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) <= 10:
            self.__name = name
        else:
            raise Exception('Длина наименования товара превышает 10 символов.')

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= Item.pay_rate

    @classmethod
    def instantiate_from_csv(cls, path="items.csv"):
        """
        класс-метод, инициализирующий экземпляры класса Item данными из файла src/items.csv
        """
        csv_path = os.path.join("..", "src", ".", path)
        try:
            open(csv_path)
        except FileNotFoundError:
            print('Отсутствует файл item.csv')
        else:
            with open(csv_path) as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if len(row.values()) < 3:
                        raise InstantiateCSVError("Файл item.csv поврежден")
                    else:
                        name, price, quantity = row.values()
                        cls(name, float(price), int(quantity))

    @staticmethod
    def string_to_number(number_string: str):
        """
        Статический метод, возвращающий число из числа-строки.

        :param number_string: Число в виде строки.
        :return: Число.
        """
        return int(float(number_string))
