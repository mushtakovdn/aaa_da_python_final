from pizza import Pizza


def test_pizza_equality_1():
    """
    Проверяет функциональность сравнения двух пицц
    Кейс, когда Название, рецепт, размер равны
    """
    m1 = Pizza('Margherita', [
        'tomato sauce', 'mozzarella', 'tomatoes'], 'XL')
    m2 = Pizza('Margherita', [
        'tomato sauce', 'mozzarella', 'tomatoes'], 'XL')
    assert m1 == m2


def test_pizza_equality_2():
    """
    Проверяет функциональность сравнения двух пицц
    Кейс с разными размерами
    """
    m1 = Pizza('Margherita', [
        'tomato sauce', 'mozzarella', 'tomatoes'], 'XL')
    m2 = Pizza('Margherita', [
        'tomato sauce', 'mozzarella', 'tomatoes'], 'L')
    assert not m1 == m2


def test_pizza_equality_3():
    """
    Проверяет функциональность сравнения двух пицц
    Кейс с разными рецептами
    """
    m1 = Pizza('Margherita', [
        'tomato sauce', 'mozzarella', 'tomatoes'], 'XL')
    m2 = Pizza('Margherita', [
        'tomato sauce', 'mozzarella', 'tomatoes', 'pepperoni'], 'XL')
    assert not m1 == m2


def test_pizza_equality_4():
    """
    Проверяет функциональность сравнения двух пицц
    Кейс с разными названиями
    """
    m1 = Pizza('Margherita', [
        'tomato sauce', 'mozzarella', 'tomatoes'], 'XL')
    m2 = Pizza('Pepperoni', [
        'tomato sauce', 'mozzarella', 'tomatoes'], 'XL')
    assert not m1 == m2


def test_pizza_dict():
    m1 = Pizza('Margherita', [
        'tomato sauce', 'mozzarella', 'tomatoes'], 'XL')
    exp = {'Margherita': ['tomato sauce', 'mozzarella', 'tomatoes']}
    assert m1.dict() == exp
