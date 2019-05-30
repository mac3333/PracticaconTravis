# Testing

from ...practico_02 import ejercicio_01 as ej01

def test_rectangulo():
    rect = ej01.Rectangulo(5, 5)
    assert rect.area() == 25
