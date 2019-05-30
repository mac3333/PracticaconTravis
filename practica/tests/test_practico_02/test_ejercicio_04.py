# Testing

from ...practico_02 import ejercicio_04 as ej04

def test_estudiante():
    est = ej04.Estudiante("Ezequiel", 23, "M", 85, 168, "ISI", 2015, 28, 41)
    assert est.edad_ingreso() == 19
    assert est.avance() == "68.29%"
