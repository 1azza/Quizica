import requests
from pprint import pprint
from .utils.CookieManipulation import dictToHeader, headerToDict
from .setGen import setGenerator
import json
class Set():
    def __init__(self, set_id):
        self.set_id = set_id
        self.headers =    {
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0",
            'CS-Token': self.cookies.get('qtkn'),
            'Cookie': dictToHeader(self.cookies),
            }
        self.Myset = setGenerator(set_id)
    def setTitle(self, Title):
        url = "https://quizlet.com/webapi/3.2/sets/save"
        querystring = {"_method":"PUT"}
        payload = self.Myset.setTitle(Title)
        response = requests.request("POST", url, data=payload, headers=self.headers, params=querystring)
        return True
    def publish(self):
        url = "https://quizlet.com/webapi/3.2/sets/save"
        querystring = {"_method":"PUT"}
        payload = {
            "data": [
                {
                    "id": self.set_id,
                    "wordLang": "en"
                }
            ],
            "requestId": "1652218190262:set:op-seq-1"
        }
        response = requests.request("POST", url, data=json.dumps(payload), headers=self.headers, params=querystring)
        payload = {
            "data": [
                {
                    "id": self.set_id,
                    "defLang": "en"
                }
            ],
            "requestId": "1652219378465:set:op-seq-0"
        }
        response = requests.request("POST", url, data=json.dumps(payload), headers=self.headers, params=querystring)
        
        payload =   {
            "data": [
                    {
                        "id": self.set_id,
                        "publishedTimestamp": 1652218679
                    }
                ],
                "requestId": "1652218190262:set:op-seq-2"
                }
        response = requests.request("POST", url, data=json.dumps(payload), headers=self.headers, params=querystring)
        if response != 500:
            try:
                return response.json().get('responses')[0].get('error').get('message')
            except:
                info = response.json().get('responses')[0].get('models').get('set')[0]
                return info.get('_webUrl')
    def addCards(self, *args):
        for arg in args: # arg is a dict
            for key in arg:
                self.Myset.addCard(key, arg[key])
        
        url = "https://quizlet.com/webapi/3.2/terms/save"
        querystring = {"_method":"PUT"}
        payload = self.Myset.build()
        response = requests.request("POST", url, data=payload, headers=self.headers, params=querystring)
        data = {}
        for i in response.json().get('responses'):
            for i in i.get('models').get('term'):
                data[i.get('word')] = i.get('id')
        return data
    def saveToFolder(self, folder_id):
        url = "https://quizlet.com/webapi/3.2/folder-sets/save"
        payload = {
                    "data": [
                        {
                            "folderId": folder_id,
                            "setId": self.set_id
                        }
                    ]
                }
        response = requests.request("POST", url, data=json.dumps(payload), headers=self.headers)

