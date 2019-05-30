# Implementar la funcion crear_tabla, que cree una tabla Persona con:
# - IdPersona: Int() (autoincremental)
# - Nombre: Char(30)
# - FechaNacimiento: Date()
# - DNI: Int()
# - Altura: Int()

# Implementar la funcion borrar_tabla, que borra la tabla creada anteriormente.

import sqlite3

database = "database.db"

def create_connection():
    return sqlite3.connect(database)

def execute_query(query, parameters=tuple()):
    conn = create_connection()
    cursor = conn.cursor()

    with conn:
        result = cursor.execute(query, parameters).fetchone()

    return result

def execute_query_many(query, parameters=tuple()):
    conn = create_connection()
    cursor = conn.cursor()

    with conn:
        result = cursor.execute(query, parameters).fetchall()

    return result

def get_last_id(query, parameters=tuple()):
    conn = create_connection()
    cursor = conn.cursor()

    with conn:
        cursor.execute(query, parameters)
        lastid = cursor.lastrowid

    return lastid

def crear_tabla():

    create_table = """ 
        CREATE TABLE IF NOT EXISTS Persona (
        id integer PRIMARY KEY AUTOINCREMENT,
        name text NOT NULL,
        birth_date text,
        DNI integer,
        altura integer
    );
    """

    return execute_query(create_table)

def check_exists(id_persona):
    exists = """
    SELECT EXISTS(
        SELECT 1
        FROM Persona 
        WHERE id=?
    );
    """

    exists = execute_query(exists, (id_persona,))

    return 1 in exists


def borrar_tabla():
    drop_table = " DROP TABLE IF EXISTS Persona; "

    execute_query(drop_table)


# no modificar
def reset_tabla(func):
    def func_wrapper():
        crear_tabla()
        func()
        borrar_tabla()
    return func_wrapper
