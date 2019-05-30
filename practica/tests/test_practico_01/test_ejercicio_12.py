# Testing

from ...practico_01.ejercicio_12 import suma

def test_zero():
    assert suma(0) == 0

def test_one():
    assert suma(1) == 1

def test_positive():
    assert suma(5) == 15
