import pytest
from src.keyboard import Keyboard


@pytest.fixture
def item_keyboard():
    return Keyboard('Dark Project KD87A', 9600, 5)


def test_keyboard_init(item_keyboard):
    assert item_keyboard.name == "Dark Project KD87A"
    assert item_keyboard.price == 9600
    assert item_keyboard.quantity == 5


def test_change_lang(item_keyboard):
    assert str(item_keyboard.language) == "EN"
    item_keyboard.change_lang()
    assert str(item_keyboard.language) == "RU"
    item_keyboard.change_lang()
    assert str(item_keyboard.language) == "EN"
