# Testing

from ...practico_02 import ejercicio_03 as ej03

def test_persona():
    per = ej03.Persona("Ezequiel", 23, "M", 85, 168)
    assert per.dni == "00000001"

    per = ej03.Persona("Francisco", 40, "M", 70, 158)
    assert per.dni == "00000002"
