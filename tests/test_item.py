import pytest
from src.item import Item
from src.item import InstantiateCSVError


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


def test_repr(item_smartphone):
    assert repr(item_smartphone) == "Item('Смартфон', 10000, 20)"


def test_str(item_smartphone):
    assert str(item_smartphone) == 'Смартфон'


def test_add(item_smartphone):
    assert item_smartphone + item_smartphone == 40
    with pytest.raises(ValueError):
        item_smartphone + 10


def test_errors():
    with pytest.raises(InstantiateCSVError):
        Item.instantiate_from_csv("items_test.csv")
