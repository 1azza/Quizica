from pprint import pprint
from .user import User
from .set import Set
import logging
import requests
s = requests.session()
class Quizlet:
    def __init__(self, username, password):
        self.user = User(s , username, password)
        cookies = self.user.login()
        logging.debug(cookies)
        self.set = Set(s, cookies)
