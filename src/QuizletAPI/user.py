import requests
from pprint import pprint
import logging
from utils.CookieManipulation import dictToHeader, headerToDict
import json
class User():
    def __init__(self, cookies, username, password):
        self.cookies = cookies
        self.username = username
        self.password = password
    def login(self):
        url = "https://quizlet.com/login"
        cookies = dictToHeader(self.cookies)
        # print(cookies)
        querystring = {"redir":"https://quizlet.com/latest"}
        payload = "{\"password\":\""+self.password+"\",\"username\":\""+self.username+"\"}"
        self.headers = {
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0",
            'Accept': "application/json",
            'Accept-Language': "en-GB,en;q=0.5",
            'Referer': "https://quizlet.com/login?redir=https://quizlet.com/latest",
            'CS-Token': "G2FdR2FnEsVKpwtTMGuG2q",
            'x-requested-with': "XMLHttpRequest",
            'Content-Type': "application/json",
            'Origin': "https://quizlet.com",
            'Connection': "keep-alive",
            'Cookie': cookies,
            'Sec-Fetch-Dest': "empty",
            'Sec-Fetch-Mode': "cors",
            'Sec-Fetch-Site': "same-origin",
            'Pragma': "no-cache",
            'Cache-Control': "no-cache",
            'TE': "trailers"
            }
        response = requests.request("POST", url, data=payload, headers=self.headers, params=querystring)
        if response.status_code == 200:
            print(f'Sucsess={response.json().get("success")}')
            qlts = response.cookies.get_dict().get('qlts')
            self.cookies['qlts'] = qlts
            self.headers['Cookie'] = dictToHeader(self.cookies)
            return qlts
            
            
        elif response.status_code == 403:
            print('Captcha has been triggered, please try again later.') 
        else:
            print('Unknown error.')
        return False
    def getFolders(self):

        url = "https://quizlet.com/gb/698456950/eukaryotes-prokaryotes-flash-cards"
        querystring = {"funnelUUID":"9811eadf-f14b-4add-9831-f7bdeb24398a"}
        payload = ""
        response = requests.request("GET", url, data=payload, headers=self.headers, params=querystring)
        print(response.text)
    def createSet(self):
        url = "https://quizlet.com/webapi/3.2/sets/save"
        querystring = {"_method":"PUT"}
        payload =   {
            "data": [
                {
                    "accessType": 2,
                    "description": "Powered by https://github.com/1azza/quizica"
                }
            ],
            "requestId": "1652221170773:set:op-seq-0"
        }
        response = requests.request("POST", url, data=json.dumps(payload), headers=self.headers, params=querystring)
        return response.json().get('responses')[0].get('models').get('set')[0].get('id')