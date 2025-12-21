from src.classes import Product, Category


def test_init_product1(test_product1):
    assert test_product1.name == 'Samsung Galaxy S23 Ultra'
    assert test_product1.description == '256GB, Серый цвет, 200MP камера'
    assert test_product1.price == 180000.0
    assert test_product1.quantity == 5


def test_init_category(test_category1):
    assert test_category1.name == 'Смартфоны'
    assert test_category1.description == 'Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни'
    assert test_category1.products == ["product1", "product2", "product3"]
    assert test_category1.category_count == 1
    assert test_category1.product_count == 3
