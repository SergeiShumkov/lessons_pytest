import requests

from src.schemas.user import User
from configuration import SERVICE_URL
from src.baseclasses.response import Response


resp = requests.get(SERVICE_URL)


# def test_1():
#     # print(resp.json())
#     # print(resp.__getstate__())
#     print("\n ", resp.url, "\n ", resp.encoding)



def test_getting_users_list():
    response = requests.get(SERVICE_URL)
    test_object = Response(response)
    test_object.assert_status_code(300).validate(User)