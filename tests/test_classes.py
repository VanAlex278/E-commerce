import pytest

from src.classes import Product, Category


def test_init_product1(capsys, test_product1):
    assert test_product1.name == 'Samsung Galaxy S23 Ultra'
    assert test_product1.description == '256GB, Серый цвет, 200MP камера'
    assert test_product1.price == 180000.0
    assert test_product1.quantity == 5
    assert str(test_product1) == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."
    test_product1.price = 800
    assert test_product1.price == 800
    test_product1.price = 0
    message = capsys.readouterr()
    assert message.out.strip().split('\n')[-1] == "Цена не должна быть нулевая или отрицательная"
    assert test_product1.price == 800
    new_product = Product.new_product(
        {"name": "Iphone 15", "description": "512GB, Gray space", "price": 123000.0,
         "quantity": 7})
    assert new_product.name == "Iphone 15"
    assert new_product.description == "512GB, Gray space"
    assert new_product.price == 123000.0
    assert new_product.quantity == 7
    assert test_product1 + new_product == 865000.0


def test_init_category(test_category1):
    assert test_category1.name == 'Смартфоны'
    assert test_category1.description == ('Смартфоны, как средство не только коммуникации,'
                                          ' но и получения дополнительных функций для удобства жизни')
    assert str(test_category1) == 'Смартфоны, количество продуктов: 27 шт.'
    assert test_category1.products == ('Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\n'
                                       'Iphone 15, 210000.0 руб. Остаток: 8 шт.\n'
                                       'Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.\n')
    assert test_category1.category_count == 1
    assert test_category1.product_count == 146


def test_init_smartphone(test_product_smartphone1):
    assert test_product_smartphone1.name == "Iphone 15"
    assert test_product_smartphone1.description == "512GB, Gray space"
    assert test_product_smartphone1.price == 210000.0
    assert test_product_smartphone1.quantity == 8
    assert test_product_smartphone1.efficiency == 98.2
    assert test_product_smartphone1.model == "15"
    assert test_product_smartphone1.memory == 512
    assert test_product_smartphone1.color == "Gray space"


def test_summ_smartphone(test_product_smartphone1, test_product_smartphone2):
    assert test_product_smartphone1 + test_product_smartphone2 == 2114000.0


def test_summ_error(test_product_smartphone1, test_product_lawnglass1):
    with pytest.raises(TypeError):
        test_product_smartphone1 + test_product_lawnglass1


def test_init_lawngrass(test_product_lawnglass1):
    assert test_product_lawnglass1.name == "Газонная трава"
    assert test_product_lawnglass1.description == "Элитная трава для газона"
    assert test_product_lawnglass1.price == 500.0
    assert test_product_lawnglass1.quantity == 20
    assert test_product_lawnglass1.country == "Россия"
    assert test_product_lawnglass1.germination_period == "7 дней"
    assert test_product_lawnglass1.color == "Зеленый"


def test_add_product_error(test_category1):
    with pytest.raises(TypeError):
        test_category1.add_product(1)


def test_add_product_error2(capsys):
    with pytest.raises(ValueError):
        Product("Бракованный товар", "Неверное количество", 1000.0, 0)


def test_print_mixin(capsys):
    Product(
        name="Samsung Galaxy S23 Ultra",
        description="256GB, Серый цвет, 200MP камера",
        price=180000.0,
        quantity=5
    )
    message = capsys.readouterr()
    assert message.out.split('\n')[0] == 'Product(Samsung Galaxy S23 Ultra, 256GB, Серый цвет, 200MP камера, 180000.0, 5)'


def test_middle_price(test_category1):
    assert test_category1.middle_price() == 140333.33


def test_middle_price_zero():
    category_empty = Category("Пустая категория", "Категория без продуктов", [])
    assert category_empty.middle_price() == 0
