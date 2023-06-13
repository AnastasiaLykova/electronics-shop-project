import pytest
from src.item import Item


@pytest.fixture
def item_smartphone():
    return Item("Смартфон", 10000, 20)


def test_item_init(item_smartphone):
    assert item_smartphone.name == "Смартфон"
    assert item_smartphone.price == 10000
    assert item_smartphone.quantity == 20
    with pytest.raises(Exception):
        item_smartphone.name = "СуперСмартфон"
    assert item_smartphone.name == "Смартфон"
    item_smartphone.name = "Телефон"
    assert item_smartphone.name == "Телефон"


def test_calculate_total_price(item_smartphone):
    assert item_smartphone.calculate_total_price() == 200000


def test_apply_discount(item_smartphone):
    Item.pay_rate = 0.8
    item_smartphone.apply_discount()
    assert item_smartphone.price == 8000.0


def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5
