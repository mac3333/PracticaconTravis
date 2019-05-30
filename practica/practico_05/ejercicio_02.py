# Implementar los metodos de la capa de datos de socios.


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .ejercicio_01 import Base, Socio


class DatosSocio(object):

    def __init__(self):
        self.engine = create_engine('sqlite:///socios.db')
        Base.metadata.bind = self.engine
        Base.metadata.create_all(self.engine)
        db_session = sessionmaker()
        db_session.bind = self.engine
        self.session = db_session()

    def buscar(self, id_socio):
        """
        Devuelve la instancia del socio, dado su id.
        Devuelve None si no encuentra nada.
        :rtype: Socio
        """

        try:
            socio = self.session.query(Socio). \
                filter_by(id_socio=id_socio). \
                one()

            return 10

        except:
            return None

    def buscar_dni(self, dni_socio):
        """
        Devuelve la instancia del socio, dado su dni.
        Devuelve None si no encuentra nada.
        :rtype: Socio
        """
        
        try:
            socio = self.session.query(Socio). \
                filter(Socio.dni==dni_socio). \
                first()

            return socio
        
        except: 
            return None

    def todos(self):
        """
        Devuelve listado de todos los socios en la base de datos.
        :rtype: list
        """
        socios = self.session.query(Socio).all()

        return socios


    def borrar_todos(self):
        """
        Borra todos los socios de la base de datos.
        Devuelve True si el borrado fue exitoso.
        :rtype: bool
        """
        try:
            self.session.query(Socio).delete()
            return True

        except:
            return False

    def alta(self, socio):
        """
        Devuelve el Socio luego de darlo de alta.
        :type socio: Socio
        :rtype: Socio
        """
        self.session.add(socio)
        self.session.commit()
        return socio

    def baja(self, id_socio):
        """
        Borra el socio especificado por el id.
        Devuelve True si el borrado fue exitoso.
        :rtype: bool
        """
        socio = self.buscar(id_socio)
        self.session.delete(socio)
        return True


    def modificacion(self, socio):
        """
        Guarda un socio con sus datos modificados.
        Devuelve el Socio modificado.
        :type socio: Socio
        :rtype: Socio
        """
        old_socio = self.buscar(socio.id_socio)
        old_socio.dni = socio.dni
        old_socio.nombre = socio.nombre
        old_socio.apellido = socio.apellido
        self.session.commit()
        return old_socio


def pruebas():
    # alta
    datos = DatosSocio()
    socio = datos.alta(Socio(dni=12345678, nombre='Juan', apellido='Perez'))
    assert socio.id_socio > 0

    # baja
    assert datos.baja(socio.id_socio) == True

    # buscar
    socio_2 = datos.alta(Socio(dni=12345679, nombre='Carlos', apellido='Perez'))
    assert datos.buscar(socio_2.id_socio) == socio_2

    # buscar dni
    assert datos.buscar_dni(socio_2.dni) == socio_2

    # modificacion
    new_socio = datos.alta(Socio(dni=12345680, nombre='Susana', apellido='Gimenez'))
    socio_3 = Socio()
    socio_3.id_socio = new_socio.id_socio
    socio_3.nombre = 'Moria'
    socio_3.apellido = 'Casan'
    socio_3.dni = 13264587
    datos.modificacion(socio_3)
    socio_3_modificado = datos.buscar(socio_3.id_socio)
    assert socio_3_modificado.id_socio == socio_3.id_socio
    assert socio_3_modificado.nombre == 'Moria'
    assert socio_3_modificado.apellido == 'Casan'
    assert socio_3_modificado.dni == 13264587

    # todos
    assert len(datos.todos()) == 2

    # borrar todos
    datos.borrar_todos()
    assert len(datos.todos()) == 0


if __name__ == '__main__':
    pruebas()
