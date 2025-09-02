# tests/test_data.py
import random
from data import tarjetas  # o las funciones que tengas

def test_terms_structure():
    assert isinstance(tarjetas, list)
    assert len(tarjetas) > 0
    for t in tarjetas:
        assert 'termino' in t
        assert 'definicion' in t

# Si tienes funciones helpers:
# from data import get_terms_by_category, get_random_term
# def test_get_random_term():
#     term = get_random_term()
#     assert isinstance(term, dict) and 'termino' in term
