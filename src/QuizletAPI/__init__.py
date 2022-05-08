from pprint import pprint
from .login import login
from .set import Set
import logging
class Quizlet:
    def __init__(self, username, password):
        cookies = login(username, password)
        logging.debug(cookies)
        self.set = Set(cookies)