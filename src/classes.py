from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """Абстрактный метод"""

    @abstractmethod
    def __init__(self):
        pass


class PrintMixin:
    def __init__(self):
        print(repr(self))

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}, {self.description}, {self.price}, {self.quantity})"


class Product(PrintMixin, BaseProduct):
    """Класс для продуктов"""

    name: str  # название
    description: str  # описание
    price: float  # цена
    quantity: int  # количество в наличии

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price
        if quantity > 0:
            self.quantity = quantity
        elif quantity == 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")
        super().__init__()

    def __str__(self):
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if type(self) == type(other):
            return self.__price * self.quantity + other.__price * other.quantity
        else:
            raise TypeError

    @classmethod
    def new_product(cls, new_object: dict):
        """Метод, возвращет созданный объект класса"""

        name, description, price, quantity = new_object.values()
        return cls(name, description, price, quantity)

    @property
    def price(self):
        """Геттер возвращает значение приватного атрибута цены"""

        return self.__price

    @price.setter
    def price(self, new_price: float):
        """Сеттер устанавливает новое значение приватного атрибута цены"""

        if new_price > 0:
            self.__price = new_price
        else:
            print("Цена не должна быть нулевая или отрицательная")


class Smartphone(Product):
    name: str
    description: str
    price: float
    quantity: int
    efficiency: float
    model: str
    memory: int
    color: str

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: float,
        model: str,
        memory: int,
        color: str,
    ):
        """Инициализация Smartphone"""

        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    name: str
    description: str
    price: float
    quantity: int
    country: str
    germination_period: str
    color: str

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: str,
        color: str,
    ):
        """Инициализация LawnGrass"""

        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color


class Category:
    """Класс для категорий"""

    name: str  # название
    description: str  # описание
    products: list  # список товаров продуктов

    # Переменная на уровне класса для подсчета количества категорий и товаров
    category_count = 0  # количество категорий
    product_count = 0  # количество товаров

    def __init__(self, name: str, description: str, products: list):
        """Метод, который инициализирует экземпляры класса."""
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(self.products)

    def __str__(self):
        count = 0
        for product in self.__products:
            count += int(product.quantity)
        return f"{self.name}, количество продуктов: {count} шт."

    def add_product(self, other):
        if isinstance(other, Product):
            self.__products.append(other)
            Category.product_count += 1
        else:
            raise TypeError

    @property
    def products(self):
        """Выводить списка товаров в виде строки"""

        product_str = ""
        for product in self.__products:
            product_str += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return product_str

    def middle_price(self):
        """Функция для подсчета средней цены продуктов."""
        try:
            return round(sum([product.price for product in self.__products]) / len(self.__products), 2)
        except ZeroDivisionError:
            return 0
