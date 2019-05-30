# Testing

from ...practico_01.ejercicio_13 import es_primo

def test_one():
    assert es_primo(1) is True

def test_prime():
    assert es_primo(17) is True

def test_non_prime():
    assert es_primo(18) is False