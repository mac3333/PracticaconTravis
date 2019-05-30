# Testing

from ...practico_01.ejercicio_04 import is_vocal

# Classical

def test_vowel():
    assert is_vocal('a') is True
    assert is_vocal('e') is True
    assert is_vocal('i') is True
    assert is_vocal('o') is True
    assert is_vocal('u') is True

def test_non_vowel():
    assert is_vocal('g') is False
