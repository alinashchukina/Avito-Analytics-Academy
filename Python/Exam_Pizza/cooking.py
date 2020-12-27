import random
from pizza import Pizza
from typing import Callable
from functools import wraps


def log(params: str) -> Callable:
    """Параметрический декоратор, в котором параметр - это шаблон
    для названия функции, названия пиццы и времени исполнения"""

    def outer_wrapper(func: Callable) -> Callable:
        @wraps(func)
        def inner_wrapper(pizza: Pizza) -> str:
            """Внутренняя функция, которая возвращает шаблон
            с названием функции, названием пиццы и временем исполнения"""
            result = func(pizza)
            return params.format(func.__name__, pizza.name, result)

        return inner_wrapper

    return outer_wrapper


@log("We {} 🔪 your favourite {}. Wait for {} min ⏳, please!")
def bake(pizza: Pizza) -> int:
    """Готовит пиццу"""
    if pizza.size == "XL":
        return random.randint(10, 15)
    else:
        return random.randint(5, 10)


@log("We {} 🛵 your favourite {}. Wait for {} min ⏳, please!")
def deliver(pizza: Pizza) -> int:
    """Доставляет пиццу"""
    return random.randint(20, 30)


@log("You can {} 🚘 your favourite {} in {} min ⌛️, please!")
def pickup(pizza: Pizza) -> int:
    """Самовывоз"""
    return random.randint(1, 5)
