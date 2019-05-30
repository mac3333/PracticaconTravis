# Testing

import datetime

from ...practico_03.ejercicio_01 import reset_tabla, check_exists, execute_query
from ...practico_03.ejercicio_02 import agregar_persona
from ...practico_03.ejercicio_04 import buscar_persona
from ...practico_03.ejercicio_05 import actualizar_persona

@reset_tabla
def test_update():
    id_juan = agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
    actualizar_persona(id_juan, 'juan carlos perez', datetime.datetime(1988, 4, 16), 32165497, 181)
    assert buscar_persona(id_juan) == (1, 'juan carlos perez', datetime.datetime(1988, 4, 16), 32165497, 181)
    
@reset_tabla    
def test_wrong_id():
    assert actualizar_persona(123, 'nadie', datetime.datetime(1988, 4, 16), 12312312, 181) is False

