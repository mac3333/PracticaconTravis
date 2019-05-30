# Testing

import datetime

from ...practico_03.ejercicio_01 import reset_tabla, execute_query, check_exists
from ...practico_03.ejercicio_02 import agregar_persona
from ...practico_03.ejercicio_03 import borrar_persona

@reset_tabla
def test_wrong_id():
    assert borrar_persona(12345) is False

@reset_tabla
def test_delete():
    assert borrar_persona(agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)) 
