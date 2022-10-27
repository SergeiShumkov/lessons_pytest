import pytest

from calculator import calculator

def test_plus():
    assert calculator('2+2') == 4

def test_no_signs():
    with pytest.raises(ValueError) as error:
        calculator('abracadabra')
    assert ('Выражение должно содержать хотя бы один знак(+-/*)') == error.value.args[0]

def test_not_string():
    with pytest.raises(TypeError) as error:
        calculator(2)
    # print()
    # print(error.value.args[0])
    assert ("argument of type 'int' is not iterable") == error.value.args[0]
