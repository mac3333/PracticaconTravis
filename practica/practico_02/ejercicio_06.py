# Implementar la clase Persona con un constructor donde reciba una fecha de nacimiento.
# La clase además debe contener un método edad, que no recibe nada y devuelva la edad de la
# persona (entero).
# Para obtener la fecha actual, usar el método de clase "now" de la clase datetime (ya importada).

import datetime

class Persona:

    # nacimiento es un objeto datetime.datetime
    def __init__(self, nacimiento):
        self.nacimiento = nacimiento

    def edad(self):
        birth_date = datetime.datetime.strptime(self.nacimiento, '%Y.%m.%d')
        today = datetime.date.today()
        years = today.year - birth_date.year
        
        age = years

        if not all((x >= y) for x, y in zip(today.timetuple(), birth_date.timetuple())):
            age = years - 1
        
        return age
