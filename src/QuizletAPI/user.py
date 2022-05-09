import requests
from pprint import pprint
import logging
from utils.CookieManipulation import dictToHeader, headerToDict

class User():
    def __init__(self, cookies, username, password):
        self.cookies = cookies
        self.username = username
        self.password = password
    def login(self):
        url = "https://quizlet.com/login"
        cookies = dictToHeader(self.cookies)
        querystring = {"redir":"https://quizlet.com/latest"}
        payload = "{\"password\":\"Larry1102\",\"username\":\"larryrennoldson\"}"
        headers = {
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
        response = requests.request("POST", url, data=payload, headers=headers, params=querystring)
        print(response.json())
        return response.cookies.get_dict()