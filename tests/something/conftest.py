import pytest


@pytest.fixture
def get_testing_scenarios(request):
    if request.param == 'scenario_1':
        return {'name': 'Jhon'}
    elif request.param == 'scenario_2':
        return {'name': 'Ann'}
    else:
        return {'name': 'Anton'}


# def _magic_method():
#     return 17

# @pytest.fixture
# def get_magic_method():
#     return _magic_method

@pytest.fixture
def get_magic_method(get_number):
    print()
    print(f"Get number: {get_number}")
    def _wrapped(additional_number):
        return additional_number + get_number
    return _wrapped