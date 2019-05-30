# Implementar la funcion borrar_persona, que elimina un registro en la tabla Persona.
# Devuelve un booleano en base a si encontro el registro y lo borro o no.

import datetime

from .ejercicio_01 import reset_tabla, execute_query, check_exists
from .ejercicio_02 import agregar_persona


def borrar_persona(id_persona):

    if not check_exists(id_persona):
        return False

    delete_query = """
    DELETE FROM Persona
    WHERE id = ?;
    """

    return execute_query(delete_query, (id_persona,)) is None


@reset_tabla
def pruebas():
    assert borrar_persona(agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)) 
    assert borrar_persona(12345) is False

if __name__ == '__main__':
    pruebas()
