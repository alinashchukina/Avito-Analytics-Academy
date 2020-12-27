from pizza import Margherita, Pepperoni, Hawaiian
from cooking import bake, deliver, pickup
from cli import order, menu
from unittest.mock import patch
from click.testing import CliRunner
import random


def test_dict():
    """Тестирует метод dict"""
    assert Hawaiian(size="L").dict() == {
        "🥫 tomato sauce": 150,
        "🧀 mozzarella": 100,
        "🍗 chicken": 75,
        "🍍 pineapples": 50,
    }
    assert Pepperoni(size="XL").dict() == {
        "🥫 tomato sauce": 300,
        "🧀 mozzarella": 200,
        "🥓 pepperoni": 140,
    }
    assert "🍅 tomatoes" in Margherita().dict()


def test_eq():
    """Тестирует метод eq"""
    assert Pepperoni(size="XL") == Pepperoni(size="XL")
    assert Pepperoni(size="L") != Pepperoni(size="XL")
    assert Pepperoni(size="XL") != Hawaiian(size="XL")
    assert Pepperoni(size="XL") != Margherita(size="L")


def test_bake():
    """Тестирует функцию bake до применения декоратора"""
    assert bake.__wrapped__(Margherita(size="XL")) in range(10, 16)
    assert bake.__wrapped__(Margherita(size="L")) in range(5, 11)


def test_deliver():
    """Тестирует функцию deliver до применения декоратора"""
    assert deliver.__wrapped__(Margherita(size="XL")) in range(20, 31)


def test_pickup():
    """Тестирует функцию pickup до применения декоратора"""
    assert pickup.__wrapped__(Hawaiian()) in range(1, 6)


def test_bake_with_decorator():
    """Тестирует функцию bake с декоратором"""
    my_randint = 9
    with patch.object(random, "randint", return_value=my_randint):
        assert (
            bake(Margherita()) == "We bake 🔪 your favourite Margherita 🧀. "
            "Wait for 9 min ⏳, please!"
        )


def test_deliver_with_decorator():
    """Тестирует функцию bake с декоратором"""
    my_randint = 24
    with patch.object(random, "randint", return_value=my_randint):
        assert (
            deliver(Hawaiian()) == "We deliver 🛵 your favourite Hawaiian 🍍. "
            "Wait for 24 min ⏳, please!"
        )


def test_pickup_with_decorator():
    """Тестирует функцию bake с декоратором"""
    my_randint = 4
    with patch.object(random, "randint", return_value=my_randint):
        assert (
            pickup(Pepperoni()) == "You can pickup 🚘 your favourite "
            "Pepperoni 🍕 in 4 min ⌛️, please!"
        )


def test_order_with_delivery():
    """Тестирует заказ в пиццерии"""
    my_randint_deliver = 21
    with patch.object(random, "randint", return_value=my_randint_deliver):
        runner = CliRunner()
        result = runner.invoke(order, ["Margherita", "--delivery", "--size=L"])
        assert (
            "We deliver 🛵 your favourite Margherita 🧀. " +
            "Wait for 21 min ⏳, please!\n" in result.output
        )


def test_order_without_delivery():
    """Тестирует заказ в пиццерии"""
    my_randint_pickup = 5
    with patch.object(random, "randint", return_value=my_randint_pickup):
        runner = CliRunner()
        result = runner.invoke(order, ["Pepperoni", "--size=L"])
        assert (
            "You can pickup 🚘 your favourite Pepperoni 🍕 in 5 min ⌛️," +
            " please!\n" in result.output
        )


def test_menu():
    """Тестирует вывод меню пиццерии"""
    runner = CliRunner()
    result = runner.invoke(menu)
    assert (
        result.output == "- Margherita 🧀: 🥫 tomato sauce, 🧀 mozzarella, 🍅 tomatoes\n" +
        "- Pepperoni 🍕: 🥫 tomato sauce, 🧀 mozzarella, 🥓 pepperoni\n" +
        "- Hawaiian 🍍: 🥫 tomato sauce, 🧀 mozzarella, 🍗 chicken, " +
        "🍍 pineapples\n"
    )
