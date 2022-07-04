"""
Module docstring. Write something clever.
"""
from unittest import TestCase
from src.examplepackage.example_module import Aclass


class TestAclass(TestCase):
    """
    Class docstring. Write something clever.
    Maybe something about inputs and outputs.
    """
    def setUp(self):
        """ set up for tests. """
        self.aclass = Aclass(first_variable=0)

    def tearDown(self):
        """ tear down after tests. """
        return None

    def test_set_a(self):
        """ this is a test. """
        expected = 2
        self.aclass.set_a(first_variable=expected)
        result = self.aclass.first_variable
        self.assertEqual(
            first=expected,
            second=result
        )

    def test_set_b(self):
        """ this is a test. """
        expected = 2
        self.aclass.set_b(second_variable=expected)
        result = self.aclass.second_variable
        self.assertEqual(
            first=expected,
            second=result
        )

    def test_add(self):
        """ this is a test. """
        expected = 2
        result = self.aclass.add()
        self.assertEqual(
            first=expected,
            second=result
        )
