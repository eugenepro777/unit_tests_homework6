import pytest
from task_01 import ListStatistics, ListComparer


# Фикстуры для подготовки данных

@pytest.fixture
def empty_list():
    """Для создания пустого списка"""
    return []


@pytest.fixture
def non_empty_list_asc():
    """Для создания первого списка"""
    return [1, 2, 3, 4, 5]


@pytest.fixture
def non_empty_list_desc():
    """Для создания второго списка"""
    return [6, 5, 4, 3, 2]


@pytest.fixture
def list_comparer_fixture(non_empty_list_asc, empty_list):
    """Для проверки класса ListComparer"""
    return ListComparer(non_empty_list_asc, empty_list)


# Юнит-тесты для класса ListStatistics


def test_calculate_average_empty_list(empty_list):
    """Тест для вычисления среднего значения с пустым списком."""
    stats = ListStatistics(empty_list)
    assert stats.calculate_average() == 0


def test_calculate_average_empty_list_asc(non_empty_list_asc):
    """Тест для вычисления среднего значения с первым непустым списком с возрастающими значениями"""
    stats = ListStatistics(non_empty_list_asc)
    assert stats.calculate_average() == 3.0


def test_calculate_average_empty_list_desc(non_empty_list_desc):
    """Тест для вычисления среднего значения со вторым непустым списком с убывающими значениями"""
    stats = ListStatistics(non_empty_list_desc)
    assert stats.calculate_average() == 4.0


# Юнит-тесты для класса ListComparer


def test_compare_averages_first_list_larger(non_empty_list_desc, non_empty_list_asc):
    """Тест, когда среднее значение первого списка больше."""
    comparer = ListComparer(non_empty_list_desc, non_empty_list_asc)
    assert comparer.compare_averages() == "Первый список имеет большее среднее значение"


def test_compare_averages_second_list_larger(non_empty_list_asc, non_empty_list_desc):
    """Тест, когда среднее значение второго списка больше."""
    comparer = ListComparer(non_empty_list_asc, non_empty_list_desc)
    assert comparer.compare_averages() == "Второй список имеет большее среднее значение"


def test_compare_averages_equal_averages(non_empty_list_asc):
    """Тест, когда средние значения равны."""
    comparer = ListComparer(non_empty_list_asc, non_empty_list_asc)
    assert comparer.compare_averages() == "Средние значения равны"

# Параметризованные тесты


@pytest.mark.parametrize("numbers, expected_average", [([], 0), ([1, 2, 3, 4, 5], 3.0)])
def test_calculate_average(numbers, expected_average):
    """Тест для функции calculate_average с параметризацией (один из списков пустой или имеет одно значение)."""
    stats = ListStatistics(numbers)
    assert stats.calculate_average() == expected_average

# Интеграционные тесты


def test_integration_compare_averages_first_list_larger(list_comparer_fixture):
    """Интеграционный тест, когда среднее значение первого списка больше."""
    assert list_comparer_fixture.compare_averages() == "Первый список имеет большее среднее значение"


