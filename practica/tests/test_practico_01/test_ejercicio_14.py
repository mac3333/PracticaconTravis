# Testing

from ...practico_01.ejercicio_14 import resolver

def test_with_solution():
    
    matrix = [
        [False, True, False],
        [False, True, False],
        [False, False, False]
    ]

    start = (0, 0)
    end = (0, 2) 

    assert resolver(matrix, start, end) == [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2), (1, 2), (0, 2)]


def test_without_solution():

    matrix = [
        [False, True, False],
        [False, True, False],
        [False, True, False]
    ]

    start = (0, 0)
    end = (0, 2) 

    assert resolver(matrix, start, end) == "No tiene Solución"
