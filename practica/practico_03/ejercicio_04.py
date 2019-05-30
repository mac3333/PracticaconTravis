# Implementar la funcion buscar_persona, que devuelve el registro de una persona basado en su id.
# El return es una tupla que contiene sus campos: id, nombre, nacimiento, dni y altura.
# Si no encuentra ningun registro, devuelve False.

import datetime

from .ejercicio_01 import reset_tabla, check_exists, execute_query
from .ejercicio_02 import agregar_persona


def buscar_persona(id_persona):
    
    if not check_exists(id_persona):
        return False
    
    select_query = """
    SELECT id, name, birth_date, DNI, altura
    FROM Persona
    WHERE id = ?;
    """

    id_, name, birth_date, DNI, altura = execute_query(select_query, (id_persona,))

    birth_date = datetime.datetime.strptime(birth_date, '%Y-%m-%d')

    
    return id_, name, birth_date, DNI, altura


@reset_tabla
def pruebas():
    juan = buscar_persona(agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180))
    assert juan == (1, 'juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
    assert buscar_persona(12345) is False

if __name__ == '__main__':
    pruebas()
