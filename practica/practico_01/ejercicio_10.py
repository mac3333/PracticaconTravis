# Implementar las funciones superposicion_x(), que tomen dos listas y devuelva un booleano en base a
# si tienen al menos 1 elemento en común.


def mas_larga(xs):
    return sorted(xs, key=len, reverse=True)[0] if xs else []
