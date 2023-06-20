import pytest
from src.phone import Phone


@pytest.fixture
def phone_object():
    return Phone("iPhone 14", 120_000, 5, 2)


def test_phone_init(phone_object):
    assert str(phone_object) == 'iPhone 14'
    assert repr(phone_object) == "Phone('iPhone 14', 120000, 5, 2)"
    assert phone_object.number_of_sim == 2
    with pytest.raises(ValueError):
        phone_object.number_of_sim = 0
    phone_object.number_of_sim = 5
    assert phone_object.number_of_sim == 5
