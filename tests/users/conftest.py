import pytest
import requests

from configuration import SERVICE_URL


@pytest.fixture   #(autouse=True)
def get_users():
    response = requests.get(SERVICE_URL)
    return response