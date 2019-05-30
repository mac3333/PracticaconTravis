# Testing

from ...practico_05.ejercicio_02 import DatosSocio, Socio

def reset_table(func):
    def wrapper():
        datos = DatosSocio()
        datos.session.query(Socio).delete()
        datos.session.commit()
        func()
    return wrapper

@reset_table
def test_create():
    datos = DatosSocio()
    socio = datos.alta(Socio(dni=12345678, nombre='Juan', apellido='Perez'))
    datos.session.commit()
    assert socio.id_socio > 0

@reset_table
def test_delete():
    datos = DatosSocio()
    socio = datos.alta(Socio(dni=12345678, nombre='Juan', apellido='Perez'))
    datos.session.commit()
    assert datos.baja(socio.id_socio) == True

@reset_table
def test_search_by_id():
    datos = DatosSocio()
    socio = datos.alta(Socio(dni=12345679, nombre='Carlos', apellido='Perez'))
    datos.session.commit()
    assert datos.buscar(socio.id_socio) == socio

@reset_table
def test_search_by_dni():
    datos = DatosSocio()
    socio = datos.alta(Socio(dni=98765432, nombre='Mario', apellido='González'))
    datos.session.commit()
    assert datos.buscar_dni(socio.dni) == socio

@reset_table
def test_update():
    datos = DatosSocio()
    new_socio = datos.alta(Socio(dni=12345680, nombre='Susana', apellido='Gimenez'))
    socio = Socio()
    socio.id_socio = new_socio.id_socio
    socio.nombre = 'Moria'
    socio.apellido = 'Casan'
    socio.dni = 13264587
    datos.modificacion(socio)
    socio_modificado = datos.buscar(socio.id_socio)
    datos.session.commit()
    assert socio_modificado.id_socio == socio.id_socio
    assert socio_modificado.nombre == 'Moria'
    assert socio_modificado.apellido == 'Casan'
    assert socio_modificado.dni == 13264587

@reset_table
def test_list():
    datos = DatosSocio()
    datos.alta(Socio(dni=12345678, nombre='Juan', apellido='Perez'))
    datos.alta(Socio(dni=12345680, nombre='Susana', apellido='Gimenez'))
    datos.session.commit()
    assert len(datos.todos()) == 2

@reset_table
def test_delete_all():
    datos = DatosSocio()
    datos.alta(Socio(dni=12345678, nombre='Juan', apellido='Perez'))
    datos.alta(Socio(dni=12345680, nombre='Susana', apellido='Gimenez'))
    datos.session.commit()
    datos.borrar_todos()
    datos.session.commit()
    assert len(datos.todos()) == 0