# Implementar la funcion crear_tabla_peso, que cree una tabla PersonaPeso con:
# - IdPersona: Int() (Clave Foranea Persona)
# - Fecha: Date()
# - Peso: Int()

# Implementar la funcion borrar_tabla, que borra la tabla creada anteriormente.

from .ejercicio_01 import borrar_tabla, crear_tabla, execute_query


def crear_tabla_peso():
    create_table = """ 
        CREATE TABLE IF NOT EXISTS Peso (
        id integer PRIMARY KEY,
        idPersona integer,
        fecha text,
        peso integer,
        FOREIGN KEY(idPersona) REFERENCES Persona(id)
    );
    """

    return execute_query(create_table)


def borrar_tabla_peso():
    drop_table = " DROP TABLE IF EXISTS Peso; "

    execute_query(drop_table)


# no modificar
def reset_tabla(func):
    def func_wrapper():
        crear_tabla()
        crear_tabla_peso()
        func()
        borrar_tabla_peso()
        borrar_tabla()
    return func_wrapper
