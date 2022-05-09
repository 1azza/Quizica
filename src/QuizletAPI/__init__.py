from pprint import pprint
from .user import User
from .set import Set
from utils.getCfbm import getCfbm
import logging
import requests
s = requests.session()
class Quizlet:
    def __init__(self, username, password):
        self.cfbm = getCfbm()
        cookies = {'afUserId': '7a4e7c7f-36c6-45e6-84e6-dfa441cf76b1-p',
        'qi5': '1g2ur5no6lccf%3AnFE2qJ6P0Y90BFnjnXFO',
        'qtkn': 'G2FdR2FnEsVKpwtTMGuG2q',
        'fs': 'rbmngy', 
        'app_session_id': 'b21ca688-d008-42af-900f-32eca19e164f',
        '__cf_bm': self.cfbm,
        '_gcl_au' : '1.1.1553204724.1652035066'
        }
        self.user = User(cookies , username, password)
        temp = self.user.login()
        if temp == None:
            return None
        logging.debug(cookies)
        self.set = Set(cookies)
