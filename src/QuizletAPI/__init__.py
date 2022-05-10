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
        self.cookies = {'afUserId': '7a4e7c7f-36c6-45e6-84e6-dfa441cf76b1-p',
        'qi5': '1g2ur5no6lccf%3AnFE2qJ6P0Y90BFnjnXFO',
        'qtkn': 'G2FdR2FnEsVKpwtTMGuG2q',
        'fs': 'rbmngy', 
        'app_session_id': 'b21ca688-d008-42af-900f-32eca19e164f',
        '__cf_bm': self.cfbm,
        '_gcl_au' : '1.1.1553204724.1652035066', #Not sure if this is needed
        'OptanonConsentisGpcEnabled' : '0&datestamp=Thur+May+12+2022+18%3A40%3A54+GMT%2B0100+(British+Summer+Time)&version=6.34.0&isIABGlobal=false&hosts=&consentId=ffbfe21d-9f20-460a-86ce-e6063dae6088&interactionCount=2&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0004%3A1%2CN01%3A1%2CSTACK42%3A1&AwaitingReconsent=false&geolocation=GB%3BENG',
        }
        self.user = User(self.cookies , username, password)
        self.__Getqlts()
        Set.cookies = self.cookies
        self.Set = Set
        
        
    def __Getqlts(self):
        qlts = self.user.login()
        if qlts == False:
            return None
        else:
            self.cookies['qlts'] = qlts