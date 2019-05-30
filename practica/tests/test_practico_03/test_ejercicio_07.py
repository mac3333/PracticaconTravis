# Testing

import datetime

from ...practico_03.ejercicio_01 import execute_query, check_exists
from ...practico_03.ejercicio_02 import agregar_persona
from ...practico_03.ejercicio_06 import reset_tabla
from ...practico_03.ejercicio_07 import agregar_peso

@reset_tabla
def test_add():
    id_juan = agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
    assert agregar_peso(id_juan, datetime.datetime(2018, 5, 26), 80) > 0

@reset_tabla
def test_wrong_id():
    assert agregar_peso(200, datetime.datetime(1988, 5, 15), 80) == False

@reset_tabla
def test_wrong_date():
    id_juan = agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
    agregar_peso(id_juan, datetime.datetime(2018, 5, 26), 80)
    assert agregar_peso(id_juan, datetime.datetime(2018, 5, 16), 80) == False