# Testing

from ...practico_01.ejercicio_09 import generar_n_caracteres

def test_zero():
    assert generar_n_caracteres("h", 0) == ""

def test_one():
    assert generar_n_caracteres("h", 1) == "h"

def test_greater_than_one():
    assert generar_n_caracteres("h", 2) == "hh"