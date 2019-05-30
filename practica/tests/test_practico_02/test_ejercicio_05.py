# Testing

from ...practico_02 import ejercicio_04 as ej04
from ...practico_02 import ejercicio_05 as ej05

def test_carreras():
    est = ej04.Estudiante("Ezequiel", 23, "M", 85, 168, "ISI", 2015, 28, 41)
    est2 = ej04.Estudiante("Ezequiel", 18, "M", 80, 175, "IM", 2018, 3, 41)
    est3 = ej04.Estudiante("Ezequiel", 24, "M", 90, 190, "IQ", 2014, 30, 41)
    est4 = ej04.Estudiante("Ezequiel", 26, "M", 70, 145, "ISI", 2012, 34, 41)
    list_est = [est, est2, est3, est4]

    assert ej05.organizar_estudiantes(list_est) == {'IM': 1, 'IQ': 1, 'ISI': 2}
