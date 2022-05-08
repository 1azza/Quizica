from pprint import pprint
from .login import login
from .set import Set
class Quizlet:
    def __init__(self, username, password):
        cookies = login(username, password)
        self.set = Set(cookies)