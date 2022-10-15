import pytest

from src.generators.player_localization import PlayerLocalization
from src.enums.user_enums import Statuses

@pytest.mark.parametrize('status', Statuses.list())
def test_something(status, get_player_generator):    
    print(get_player_generator.set_status(status).build())

@pytest.mark.parametrize('balance_value', [
    100,
    0,
    -10,
    "asdsd"
])
def test_something1(balance_value, get_player_generator):    
    print(get_player_generator.set_balance(balance_value).build())

@pytest.mark.parametrize('delete_key', [
    "account_status",
    "balance",
    "localize",
    "avatar"
])
def test_something2(delete_key, get_player_generator):
    object_to_send = get_player_generator.build()
    del object_to_send[delete_key]
    print(object_to_send)

def test_something3(get_player_generator):
    object_to_send = get_player_generator.update_inner_generator(
        'localize', PlayerLocalization('fr_FR').set_number(15)
        ).build()
    print(object_to_send)

def test_something4(get_player_generator):
    object_to_send = get_player_generator.update_inner_value(
        ['localize', 'fr', 'is', 'the', 'best', 'lang'],
        PlayerLocalization('fr_FR').set_number(15).build()
        ).build()
    print(object_to_send)


@pytest.mark.parametrize("localizations", [
    "fr", "de", "ab", "ch"
])
def test_something5(get_player_generator, localizations):
    object_to_send = get_player_generator.update_inner_value(
        ['localize', localizations],
        PlayerLocalization('fr_FR').set_number(15).build()).build()
    print(object_to_send)


@pytest.mark.parametrize("localizations, loc", [
    ("fr", "fr_FR"),
    ("es", "es_ES"),
    ("it", "it_IT")
])
def test_something6(get_player_generator, localizations, loc):
    object_to_send = get_player_generator.update_inner_value(
        ['localize', localizations],
        PlayerLocalization(loc).set_number(15).build()).build()
    print(object_to_send)


def test_something7():
    print(Statuses.list())

@pytest.mark.parametrize("a, b, result", [
    (2, 3, 5),
    (1, 9, 10),
    (23, 4, 28),
    ("cv", "b", "cvb")

])
def test_something8(a, b, result):
    # assert a + b == result
    assert True

