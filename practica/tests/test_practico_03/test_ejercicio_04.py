# Testing

import datetime

from ...practico_03.ejercicio_01 import reset_tabla, check_exists, execute_query
from ...practico_03.ejercicio_02 import agregar_persona
from ...practico_03.ejercicio_04 import buscar_persona

@reset_tabla
def test_search():
    juan = buscar_persona(agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180))
    assert juan == (1, 'juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)

@reset_tabla
def test_wrong_id():
    assert buscar_persona(12345) is False
