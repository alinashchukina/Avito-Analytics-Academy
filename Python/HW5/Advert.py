from keyword import iskeyword
import json


class InsideClass:
    """
    InsideClass transforms data from JSON
    into dictionary
    Adds '_' to attributes that sounds the
    same as keywords
    """
    def __init__(self, data):
        for key, value in data.items():
            if iskeyword(key):
                key += '_'
            if isinstance(value, dict):
                self.__dict__[key] = InsideClass(value)
            else:
                self.__dict__[key] = value


class ColorizeMixin:
    """
    Mixin class for changing color into yellow
    """
    def __init__(self):
        self.style = 1
        self.color = 33
        self.back = '40m'

    def __str__(self):
        text = self.__repr__()
        return f"\033[{self.style};{self.color};{self.back} {text} \033[m"


class Advert(ColorizeMixin):
    """
    Transforms adverts into class objects
    with dynamic attribute creation
    Class stores attributes in __dict__
    Class prints titles and price in yellow
    Price has to be > 0
    """
    def __init__(self, data):
        super().__init__()
        self.__dict__.update(InsideClass(data).__dict__)

    @property
    def price(self):
        if "price" in self.__dict__ and self.__dict__["price"] > 0:
            return self.__dict__["price"]
        elif "price" in self.__dict__ and self.__dict__["price"] < 0:
            raise ValueError("price must be >= 0")
        return 0

    @price.setter
    def price(self, upd):
        if upd < 0:
            raise ValueError("price must be >= 0")
        self._price = upd

    def __getattr__(self, item):
        raise ValueError("Such attribute doesn't exist!")

    def __repr__(self):
        return f'{self.title} | {self.price} ₽'


if __name__ == "__main__":
    test_1 = """{
        "title": "iPhone X",
        "price": 100,
        "location": {
        "address": "город Самара, улица Мориса Тореза, 50",
        "metro_stations": ["Спортивная", "Гагаринская"]
        }
    }"""
    ad_test_1 = Advert(json.loads(test_1))
    print(ad_test_1.title)
    print(ad_test_1.price)
    print(ad_test_1.location.address)
    test_2 = """{
        "title": "Вельш-корги",
        "price": 1000,
        "class": "dogs",
        "location": {
        "address": "Москва, 25"
        }
    }"""
    ad_test_2 = Advert(json.loads(test_2))
    print(ad_test_2.class_)
    print(ad_test_2)
    test_3 = """{
            "title": "Вельш-корги",
            "price": -1000,
            "class": "dogs",
            "location": {
            "address": "Москва, 25"
            }
        }"""
    ad_test_3 = Advert(json.loads(test_3))
    # print(ad_test_3.price)  # this example shows exception for price <0
