from pprint import pprint
from .user import User
from .set import Set
from .utils.getCfbm import getCfbm
import logging
import requests
s = requests.session()


class Quizlet:
    def __init__(self, username, password):
        self.cfbm = getCfbm()
        self.cookies = {'afUserId': '7a4e7c7f-36c6-45e6-84e6-dfa441cf76b1-p',
                        'qi5': '1g2ur5no6lccf%3AnFE2qJ6P0Y90BFnjnXFO',
                        'qtkn': 'G2FdR2FnEsVKpwtTMGuG2q',
                        'fs': 'rbotes',
                        'app_session_id': 'b21ca688-d008-42af-900f-32eca19e164f',
                        '__cf_bm': self.cfbm,
                        '_gcl_au': '1.1.1553204724.1652035066',  # Not sure if this is needed
                        }
        self.user = User(self.cookies, username, password)
        #Sync cookies
        self.cookies = self.user.cookies
        self.__Getqlts()
        Set.cookies = self.cookies
        self.Set = Set

    def __Getqlts(self):
        qlts = self.user.login()
        if qlts == False:
            return None
        else:
            self.cookies['qlts'] = qlts
