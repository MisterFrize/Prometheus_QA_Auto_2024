import pytest
from modules.api.clients.github import GitHub

class User:
    def __init__(self, name=None, second_name=None):
        self.name = name
        self.second_name = second_name

    def create(self):
        self.name = "Dmytro"
        self.second_name = "Maltsev"

    def remove(self):
        self.name = ""
        self.second_name = ""

@pytest.fixture
def user():
    user = User()
    user.create()
    yield user
    user.remove()

@pytest.fixture
def github_api():
    return GitHub()