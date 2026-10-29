import pytest
from dividir import dividir

def test_dividir_exacta():
    assert dividir(10, 2) == 5.0

def test_dividir_negativos():
    assert dividir(-6, 2) == -3.0

def test_dividir_por_cero():
    with pytest.raises(ValueError):
        dividir(5, 0)