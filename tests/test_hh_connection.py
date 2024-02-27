import pytest
from src.hh_connection import GetHeadHunter


@pytest.fixture
def test_get_head_hunter():
    return GetHeadHunter("python", 1)


def test_str(test_get_head_hunter):
    """
    Проверка магического метода str
    """
    assert str(test_get_head_hunter) == "python"


def test_repr(test_get_head_hunter):
    """
    Проверка магического метода repr
    """
    assert repr(test_get_head_hunter) == 'GetHeadHunter(python, 1)'


def test_url(test_get_head_hunter):
    """
    Проверка работы ссылки
    """
    assert test_get_head_hunter.url == "https://api.hh.ru"


def test_error_connection():
    """
    Проверка на наличие ошибок
    """
    with pytest.raises(TypeError):
        GetHeadHunter()