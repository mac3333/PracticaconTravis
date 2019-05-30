# Implementar la funcion agregar_peso, que inserte un registro en la tabla PersonaPeso.
# Debe validar:
# - que el ID de la persona ingresada existe (reutilizando las funciones ya implementadas).
# - que no existe de esa persona un registro de fecha posterior al que queremos ingresar.

# Debe devolver:
# - ID del peso registrado.
# - False en caso de no cumplir con alguna validacion.

import datetime

from .ejercicio_02 import agregar_persona
from .ejercicio_06 import reset_tabla
from .ejercicio_01 import execute_query, check_exists


def get_last_record(id_persona):

    select_query = """
    SELECT Max(Peso.fecha)
    FROM Persona
    JOIN Peso
        ON Peso.idPersona = Persona.id
    WHERE Persona.id = ?;
    """

    last_date = execute_query(select_query, (id_persona,))[0]

    if last_date is None:
        return None

    last_date = datetime.datetime.strptime(last_date, '%Y-%m-%d')
    
    return last_date

def agregar_peso(id_persona, fecha, peso):
    
    if not check_exists(id_persona):
        return False

    last_date = get_last_record(id_persona)

    if not last_date is None and fecha < last_date:
        return False
    
    insert_query = """
    INSERT INTO Peso (idPersona, fecha, peso)
    VALUES (?, ?, ?);
    """

    data = (id_persona, 
            datetime.datetime.strftime(fecha, '%Y-%m-%d'),
            peso, 
            )

    return execute_query(insert_query, data) is None


@reset_tabla
def pruebas():
    id_juan = agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
    assert agregar_peso(id_juan, datetime.datetime(2018, 5, 26), 80) > 0
    # id incorrecto
    assert agregar_peso(200, datetime.datetime(1988, 5, 15), 80) == False
    # registro previo al 2018-05-26
    assert agregar_peso(id_juan, datetime.datetime(2018, 5, 16), 80) == False

if __name__ == '__main__':
    pruebas()
