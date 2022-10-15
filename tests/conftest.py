from email.policy import default
import pytest
from random import randrange

from src.generators.player import Player

@pytest.fixture
def get_player_generator():
    return Player()


@pytest.fixture
def get_number():
    return randrange(1, 1000, 5)

def _calculate(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return a + b
    else:
        return None

@pytest.fixture
def calculate():
    return _calculate

@pytest.fixture
def make_number():
    print("\nI'm getting number")
    number = randrange(1, 1000, 5)
    yield number
    print(f"\nNumber at home {number}")


def pytest_addoption(parser):
    parser.addoption(
        "--env",
        default="development",
        help="It is env variable where our tests will be run. Possible values:"
             "prod, development(default), qa"
    )

@pytest.fixture(autouse=True)
def getting_env(request):
    env = request.config.getoption('--env')
    yield env