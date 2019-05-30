# Testing

from ...practico_01.ejercicio_08 import superposicion

def test_common_elements():
    assert superposicion([1, 2, 3, 4], [3, 6, 9, 12]) is True

def test_no_common_elements():
    assert superposicion(list(range(10)), list(range(10, 20))) is False