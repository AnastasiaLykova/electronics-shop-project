import pytest
from src.item import Item


@pytest.fixture
def item_smartphone():
    return Item("Смартфон", 10000, 20)


def test_item_init(item_smartphone):
    assert item_smartphone.name == "Смартфон"
    assert item_smartphone.price == 10000
    assert item_smartphone.quantity == 20


def test_calculate_total_price(item_smartphone):
    assert item_smartphone.calculate_total_price() == 200000


def test_apply_discount(item_smartphone):
    Item.pay_rate = 0.8
    item_smartphone.apply_discount()
    assert item_smartphone.price == 8000.0
