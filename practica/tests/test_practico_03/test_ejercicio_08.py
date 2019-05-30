# Testing

import datetime

from ...practico_03.ejercicio_01 import execute_query_many, check_exists
from ...practico_03.ejercicio_02 import agregar_persona
from ...practico_03.ejercicio_06 import reset_tabla
from ...practico_03.ejercicio_07 import agregar_peso
from ...practico_03.ejercicio_08 import listar_pesos

@reset_tabla
def test_list():
    id_juan = agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
    agregar_peso(id_juan, datetime.datetime(2018, 5, 1), 80)
    agregar_peso(id_juan, datetime.datetime(2018, 6, 1), 85)
    pesos_juan = listar_pesos(id_juan)
    pesos_esperados = [
        ('2018-05-01', 80),
        ('2018-06-01', 85),
    ]
    assert pesos_juan == pesos_esperados
    
@reset_tabla
def test_wrong_id():
    assert listar_pesos(200) == False