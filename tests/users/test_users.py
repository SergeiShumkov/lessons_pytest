from src.schemas.user import User
from src.baseclasses.response import Response


# def test_1():
#     # print(resp.json())
#     # print(resp.__getstate__())
#     print("\n ", resp.url, "\n ", resp.encoding)

def test_getting_users_list(get_users, make_number):  # (get_users, calculate)
    Response(get_users).assert_status_code(200).validate(User)
    print(make_number)
    
    # print(calculate (1, 1))


def test_another():
    assert 1 == 1