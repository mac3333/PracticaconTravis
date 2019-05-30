# Testing

from ...practico_03.ejercicio_01 import crear_tabla, borrar_tabla

def test_create():
    crear_tabla()

def test_delete():
    borrar_tabla()

def test_table_creation():
    crear_tabla()
    borrar_tabla()
