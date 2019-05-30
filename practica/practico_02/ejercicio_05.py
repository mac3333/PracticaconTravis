# Implementar la función organizar_estudiantes() que tome como parámetro una lista de Estudiantes
# y devuelva un diccionario con las carreras como keys, y la cantidad de estudiantes en cada una de ellas como values.

from .ejercicio_04 import Estudiante
from collections import defaultdict

def organizar_estudiantes(estudiantes):
    est_dict = defaultdict(int)

    for est in estudiantes:
        est_dict[est.carrera] += 1
    
    return est_dict
