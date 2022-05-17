import requests
from .utils.CookieManipulation import dictToHeader, headerToDict
import json
from .utils.getCfbm import getCfbm

class User():
    def __init__(self, cookies, username, password):
        self.cookies = cookies
        self.username = username
        self.password = password
        self.headers = None

    def login(self):
        url = "https://quizlet.com/login"
        cookies = dictToHeader(self.cookies)
        # print(cookies)
        querystring = {"redir": "https://quizlet.com/latest"}
        payload = "{\"password\":\""+self.password + \
            "\",\"username\":\""+self.username+"\"}"
        self.headers = {
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0",
            'CS-Token': "G2FdR2FnEsVKpwtTMGuG2q",
            'x-requested-with': "XMLHttpRequest",
            'Cookie': cookies,
        }
        response = requests.request(
            "POST", url, data=payload, headers=self.headers, params=querystring)
        if response.status_code == 200:
            qlts = response.cookies.get_dict().get('qlts')
            self.cookies['qlts'] = qlts
            self.headers['Cookie'] = dictToHeader(self.cookies)
            print('Session ID:')
            # sessionID = self.__StartSession()
            # print(f'{sessionID}\n')
            # self.cookies['app_session_id'] = sessionID
                
        
        
        elif response.status_code == 403:
            print('Captcha has been triggered, please try again later.')
        else:
            print('Unknown error.')
        return False
    def __StartSession(self):
        url = "https://quizlet.com/webapi/3.2/app-session/start"
        payload = ""
        response = requests.request("GET", url, data=payload, headers=self.headers)
        print(response.cookies.get_dict())
        self.cookies['__cf_bm'] = response.cookies.get_dict().get('__cf_bm')
        return response.json().get('responses')[0].get('data').get('appSession').get('appSessionId')
    def getFolders(self):
        url = "https://quizlet.com/webapi/3.2/folders"
        querystring = {"filters[isDeleted]": "false", "filters[isHidden]": "false",
                       "filters[personId]": "256998883", "include[folder][]": "user", "page": "1"}
        payload = ""
        headers = {
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0",
            'x-requested-with': "XMLHttpRequest",
            'Cookie': getCfbm()
        }
        response = requests.request(
            "GET", url, data=payload, headers=headers, params=querystring)

        print(response.json())

    def createSet(self):
        url = "https://quizlet.com/webapi/3.2/sets/save"
        querystring = {"_method": "PUT"}
        payload = {
            "data": [
                {
                    "accessType": 2,
                    "description": "Powered by https://github.com/1azza/quizica"
                }
            ],
            "requestId": "1652221170773:set:op-seq-0"
        }
        response = requests.request("POST", url, data=json.dumps(
            payload), headers=self.headers, params=querystring)
        return response.json().get('responses')[0].get('models').get('set')[0].get('id')
