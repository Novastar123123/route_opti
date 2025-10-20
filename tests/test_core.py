from route_opti.core import greet


def test_greet_default():
    assert greet() == "Hello, traveler! Ready to explore optimal routes?"


def test_greet_custom_name():
    assert greet("Ada") == "Hello, Ada! Ready to explore optimal routes?"
