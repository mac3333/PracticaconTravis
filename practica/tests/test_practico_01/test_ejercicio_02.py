# Testing

from ...practico_01.ejercicio_02 import max_de_tres

# Classical

def test_a_greater_c_greater_b():
    assert max_de_tres(3, 1, 2) == 3

def test_a_greater_b_greater_c():
    assert max_de_tres(3, 2, 1) == 3

def test_b_greater_a_greater_c():
    assert max_de_tres(2, 3, 1) == 3

def test_b_greater_c_greater_a():
    assert max_de_tres(1, 3, 2) == 3

def test_c_greater_a_greater_b():
    assert max_de_tres(2, 1, 3) == 3

def test_c_greater_b_greater_a():
    assert max_de_tres(1, 2, 3) == 3

# Property Testing

from hypothesis import given
import hypothesis.strategies as st

@given(st.integers(), st.integers(), st.integers())
def test_identity(a, b, c):
    assert max_de_tres(a, b, c) == max_de_tres(max_de_tres(a, b, c), max_de_tres(a, b, c), max_de_tres(a, b, c))

@given(st.integers(), st.integers(), st.integers())
def test_idempotent(a, b, c):
    assert max_de_tres(a, a, a) == a

@given(st.integers(), st.integers(), st.integers())
def test_commutability(a, b, c):
    assert max_de_tres(a, b, c) == max_de_tres(b, a, c)
    assert max_de_tres(a, b, c) == max_de_tres(b, c, a)
    assert max_de_tres(a, b, c) == max_de_tres(c, a, b)
    assert max_de_tres(a, b, c) == max_de_tres(c, b, a)