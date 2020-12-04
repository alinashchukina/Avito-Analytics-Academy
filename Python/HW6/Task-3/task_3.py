from typing import List, Tuple
import unittest


def fit_transform(*args: str) -> List[Tuple[str, List[int]]]:
    """
    fit_transform(iterable)
    fit_transform(arg1, arg2, *args)
    """
    if len(args) == 0:
        raise TypeError('expected at least 1 arguments, got 0')

    categories = args if isinstance(args[0], str) else list(args[0])
    uniq_categories = set(categories)
    bin_format = f'{{0:0{len(uniq_categories)}b}}'

    seen_categories = dict()
    transformed_rows = []

    for cat in categories:
        bin_view_cat = (int(b) for b in bin_format.format(
            1 << len(seen_categories)))
        seen_categories.setdefault(cat, list(bin_view_cat))
        transformed_rows.append((cat, seen_categories[cat]))

    return transformed_rows


class TestFitTransform(unittest.TestCase):
    """
    Unittest class for fit_transform function
    """
    def test_list_equal(self):
        """
        test checks if output of fit_transform is correct
        """
        cities = ['Moscow', 'New York', 'Moscow', 'London']
        transformed_cities = fit_transform(cities)
        exp_transformed_cities = [
            ('Moscow', [0, 0, 1]),
            ('New York', [0, 1, 0]),
            ('Moscow', [0, 0, 1]),
            ('London', [1, 0, 0]),
        ]
        self.assertEqual(transformed_cities, exp_transformed_cities)

    def test_list_in(self):
        """
        test checks if output of fit_transform contains
        a part of correct answer
        """
        cities = ['Moscow', 'New York', 'Moscow', 'London'] * 10
        transformed_cities = fit_transform(cities)
        exp_city_in = ('London', [1, 0, 0])
        self.assertIn(exp_city_in, transformed_cities)

    def test_list_empty(self):
        """
        test checks if fit_transform leaves empty list empty
        """
        cities = []
        transformed_cities = fit_transform(cities)
        exp_transformed_cities = []
        self.assertEqual(transformed_cities, exp_transformed_cities)

    def test_args_equal(self):
        """
        test checks if fit_transform can get several arguments
        """
        transformed_cities = fit_transform('Moscow', 'New York',
                                           'Moscow', 'London')
        exp_transformed_cities = [
            ('Moscow', [0, 0, 1]),
            ('New York', [0, 1, 0]),
            ('Moscow', [0, 0, 1]),
            ('London', [1, 0, 0]),
        ]
        self.assertEqual(transformed_cities, exp_transformed_cities)

    def test_error_empty(self):
        """
        test checks if fit_transform raises an exception with 0 arguments
        """
        with self.assertRaises(TypeError):
            fit_transform()
