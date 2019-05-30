# Testing

from ...practico_01.ejercicio_01 import max

# Classical

def test_a_greater_b():
    assert max(1, 2) == 2

def test_b_greater_a():
    assert max(2, 1) == 2

def test_a_equal_b():
    assert max(1, 1) == 1

# Property Testing

from hypothesis import given
import hypothesis.strategies as st

@given(st.integers(), st.integers())
def test_identity(a, b):
    assert max(a, b) == max(max(a, b), max(a, b))

@given(st.integers(), st.integers())
def test_commutability(a, b):
    assert max(a, b) == max(b, a)

@given(st.integers(), st.integers())
def test_identity_element(a, b):
    assert max(a, a) == a