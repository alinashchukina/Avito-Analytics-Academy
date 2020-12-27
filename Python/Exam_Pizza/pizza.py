class Pizza:
    """Базовый класс для всех пицц"""

    def __init__(self, extra_ingredients: dict,
                 size: str = "L", name: str = None):
        self.name = name
        self.size = size
        self.ingredients = {"🥫 tomato sauce": 150, "🧀 mozzarella": 100}
        self.ingredients.update(extra_ingredients)
        if self.size == "XL":
            self.ingredients = {k: 2 * v for k, v in self.ingredients.items()}

    def dict(self) -> dict:
        """Функция, возвращающая рецепт пиццы в виде словаря"""
        return self.ingredients

    def __eq__(self, other) -> bool:
        """Функция, проверяющая, одинаковые ли две пиццы
        по набору ингридиентов и по размеру"""
        return self.ingredients == other.ingredients and \
            self.size == other.size


class Margherita(Pizza):
    """Класс, создающий пиццу Маргарита"""

    def __init__(self, size: str = "L"):
        self.name = "Margherita 🧀"
        self.extra_ingredients = {"🍅 tomatoes": 75}
        super().__init__(self.extra_ingredients, size, self.name)


class Pepperoni(Pizza):
    """Класс, создающий пиццу Пепперони"""

    def __init__(self, size: str = "L"):
        self.name = "Pepperoni 🍕"
        self.extra_ingredients = {"🥓 pepperoni": 70}
        super().__init__(self.extra_ingredients, size, self.name)


class Hawaiian(Pizza):
    """Класс, создающий Гавайскую пиццу"""

    def __init__(self, size: str = "L"):
        self.name = "Hawaiian 🍍"
        self.extra_ingredients = {"🍗 chicken": 75, "🍍 pineapples": 50}
        super().__init__(self.extra_ingredients, size, self.name)
