# Testing

from ...practico_02 import ejercicio_02 as ej02

import math

def test_circulo():
    circ = ej02.Circulo(1)
    assert circ.area() == math.pi
