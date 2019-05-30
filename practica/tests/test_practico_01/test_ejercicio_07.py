# Testing

from ...practico_01.ejercicio_07 import es_palindromo

# Classical

def test_palindrome():
    assert es_palindromo("rayar") is True

def test_non_palindrome():
    assert es_palindromo("amor") is False

# Property Testing

from hypothesis import given
import hypothesis.strategies as st

@given(st.text())
def test_double(text):
    assert es_palindromo(text + text) ==  es_palindromo(text)

@given(st.text(), st.integers(min_value=1, max_value=100))
def test_multiply(text, n):
    assert es_palindromo(text * n) ==  es_palindromo(text)