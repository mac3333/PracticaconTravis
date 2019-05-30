# Testing

import datetime

from ...practico_03.ejercicio_01 import reset_tabla, get_last_id
from ...practico_03.ejercicio_02 import agregar_persona

@reset_tabla
def test_first_record():
    id_juan = agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
    assert id_juan > 0

@reset_tabla
def test_second_record_id():
    id_juan = agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
    id_marcela = agregar_persona('marcela gonzalez', datetime.datetime(1980, 1, 25), 12164492, 195)
    assert id_juan > 0
    assert id_marcela > id_juan