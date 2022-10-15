import pytest
import allure

allure.attach

from src.schemas.user import User
from src.baseclasses.response import Response
from src.schemas.computer import Computer
from examples import computer

# def test_1():
#     # print(resp.json())
#     # print(resp.__getstate__())
#     print("\n ", resp.url, "\n ", resp.encoding)

def test_getting_users_list(get_users, make_number):  # (get_users, calculate)
    Response(get_users).assert_status_code(200).validate(User)
    # print(make_number)
    
    # print(calculate (1, 1))

@pytest.mark.development  # см. pytest.ini
@pytest.mark.production
@pytest.mark.skip('[ISSUE-23414] Issue with network connection')
# тест не будет выполняться(Указать причину), но будет отражаться в отчетах
def test_another():
    """
    In that test we try to check that 1 is equel to 2
    """
    assert 1 == 1

# def test_calculation_both_negative(calculate):
#     print(calculate(-1, -2))

# def test_calculation_one_negative(calculate):
#     print(calculate(-1, 2))

# def test_calculation_both_positive(calculate):
#     print(calculate(1, 2))

# def test_calculation_one_char(calculate):
#     print(calculate('a', -2))

# def test_calculation_two_chars(calculate):
#     print(calculate('a', 'b'))

@pytest.mark.development # pytest -s -v -k development tests/users/test_users.py
                         #  pytest -s -v -k " not development" tests/users/test_users.py
@pytest.mark.parametrize('first_value, second_value, result', [
   (1, 2, 3),
   (-1, -2, -3),
   (-1, 2, 1),
   ('b', -2, None),
   ('b', 'b', None)
])
def test_calculator(first_value, second_value, result, calculate):
    """
    In test we are testing calculating with different values(Valid and invalid)
    """ 
    assert calculate(first_value, second_value) == result

@pytest.mark.development  # см. pytest.ini
@pytest.mark.production
def test_another_failing_t():
    assert 1 == 2

def test_pydantic_object():
    comp = Computer.parse_obj(computer)
    print()
    # print(comp.detailed_info.physical.color.as_rgb_tuple())
    print(comp.schema_json())
