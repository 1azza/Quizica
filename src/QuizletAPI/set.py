import requests
from pprint import pprint
from utils.CookieManipulation import dictToHeader, headerToDict
from .setGen import setGenerator
from .user import User
class Set():
    def __init__(self, set_id):
        self.headers =    {
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0",
            'CS-Token': self.cookies.get('qtkn'),
            'Cookie': dictToHeader(self.cookies),
            }
        self.Myset = setGenerator(set_id)

        
    def addCards(self, *args):
        
        for arg in args: # arg is a dict
            for key in arg:
                self.Myset.addCard(key, arg[key])
        
        url = "https://quizlet.com/webapi/3.2/terms/save"
        querystring = {"_method":"PUT"}
        payload = self.Myset.build()
        pprint(payload)
        response = requests.request("POST", url, data=payload, headers=self.headers, params=querystring)
        return response.json()
    