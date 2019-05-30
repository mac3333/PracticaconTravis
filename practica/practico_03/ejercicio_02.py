# Implementar la funcion agregar_persona, que inserte un registro en la tabla Persona
# y devuelva los datos ingresados el id del nuevo registro.

import datetime

from .ejercicio_01 import reset_tabla, get_last_id


def agregar_persona(nombre, nacimiento, dni, altura):
    insert_query = """
    INSERT INTO Persona (
        name,
        birth_date,
        DNI,
        altura
        )

    VALUES ( ?, ?, ?, ?);
    """

    data = (nombre, 
            datetime.datetime.strftime(nacimiento, '%Y-%m-%d'),
            dni, 
            altura)

    return get_last_id(insert_query, data)


@reset_tabla
def pruebas():
    id_juan = agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
    id_marcela = agregar_persona('marcela gonzalez', datetime.datetime(1980, 1, 25), 12164492, 195)
    assert id_juan > 0
    assert id_marcela > id_juan

if __name__ == '__main__':
    pruebas()
