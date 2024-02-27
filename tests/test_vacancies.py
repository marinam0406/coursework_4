import pytest
from src.vacancies import Vacancy


@pytest.fixture
def test_vacancy():
    return Vacancy("python", 1)


def test_str(test_vacancy):
    """
    Проверка магического метода str
    """
    assert str(test_vacancy) == "python"


def test_repr(test_vacancy):
    """
    Проверка магического метода repr
    """
    assert repr(test_vacancy) == "Vacancy(('python', 1))"


def test_name_error(test_vacancy):
    """
    Проверка ошибок в названии
    """
    with pytest.raises(AttributeError):
        test_vacancy.name = "word"


def test_page_error(test_vacancy):
    """
    Проверка ошибок в количестве
    """
    with pytest.raises(AttributeError):
        test_vacancy.page = 1