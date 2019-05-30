# Testing

from ...practico_02 import ejercicio_06 as ej06

def test_edad():
    per = ej06.Persona('1995.12.14')
    assert per.edad() == 23
