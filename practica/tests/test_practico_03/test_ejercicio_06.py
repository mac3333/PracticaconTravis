# Testing

from ...practico_03.ejercicio_01 import borrar_tabla, crear_tabla, execute_query
from ...practico_03.ejercicio_06 import crear_tabla_peso, borrar_tabla_peso

def test_table_creation():
    crear_tabla_peso()

def test_table_delete():
    borrar_tabla_peso()

def test_table_management():
    crear_tabla()
    crear_tabla_peso()
    borrar_tabla_peso()
    borrar_tabla()


