# Testing

from ...practico_01.ejercicio_03 import length

# Classical

def empty_list():
    assert length([]) == 0

def non_empty_list():
    assert length([1, 2, 3]) == 3

# Property Testing

from hypothesis import given, example
import hypothesis.strategies as st

@given(st.lists(st.integers()))
@example([])
def test_identity(l):
    assert length(l) == length(l)

@given(st.lists(st.integers()), st.integers(min_value=0, max_value=100))
@example([], 10)
def test_multiply(l, n):
    assert length(l * n) == length(l) * n

@given(st.lists(st.integers()))
@example([])
def test_sum(l):
    assert length(l + l) == length(l) + length(l)
