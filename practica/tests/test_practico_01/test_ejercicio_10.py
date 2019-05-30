# Testing

from ...practico_01.ejercicio_10 import mas_larga

def test_empty():
    assert mas_larga([]) == []

def test_one_element_list():
    assert mas_larga(["hola"]) == "hola"

def test_several_element_list():
    assert mas_larga(["h", "hola", "esternocleidomastoideo", "adios"]) == "esternocleidomastoideo"