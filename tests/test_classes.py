from src.classes import Product


def test_init_product1(capsys, test_product1):
    assert test_product1.name == 'Samsung Galaxy S23 Ultra'
    assert test_product1.description == '256GB, Серый цвет, 200MP камера'
    assert test_product1.price == 180000.0
    assert test_product1.quantity == 5
    test_product1.price = 800
    assert test_product1.price == 800
    test_product1.price = 0
    message = capsys.readouterr()
    assert message.out.strip() == "Цена не должна быть нулевая или отрицательная"
    assert test_product1.price == 800
    new_product = Product.new_product(
        {"name": "Iphone 15", "description": "512GB, Gray space", "price": 123000.0,
         "quantity": 7})
    assert new_product.name == "Iphone 15"
    assert new_product.description == "512GB, Gray space"
    assert new_product.price == 123000.0
    assert new_product.quantity == 7


def test_init_category(test_category1):
    assert test_category1.name == 'Смартфоны'
    assert test_category1.description == ('Смартфоны, как средство не только коммуникации,'
                                          ' но и получения дополнительных функций для удобства жизни')
    assert test_category1.products == ('Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\n'
                                       'Iphone 15, 210000.0 руб. Остаток: 8 шт.\n'
                                       'Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.\n')
    assert test_category1.category_count == 1
    assert test_category1.product_count == 146
