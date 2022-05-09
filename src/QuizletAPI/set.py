import requests
from pprint import pprint
from utils.CookieManipulation import dictToHeader, headerToDict

class Set():
    def __init__(self, cookies):
        self.cookies = cookies
 
        
    def edit(self, title, set_id=None):
        url = "https://quizlet.com/webapi/3.2/sets/save"
        querystring = {"_method":"PUT"}
        payload = "{\"data\":[{\"id\":697661088,\"title\":\""+str(title)+"\"}],\"requestId\":\"1652038877870:set:op-seq-0\"}"
        cookie = dictToHeader(self.cookies)
        headers = {
            'cookie': "qlts=1_tj8u.05FkemE8tpQ6-sNtZK5uJtU6Dxc4e52VS8E0tdTb-Kf2C-N9tOoRlbtLNJTJwMkSLrqQYZ9Fg; app_session_id=13fa6cb9-805d-457e-8902-b3a57a71585c; __cf_bm=BUE1kSND84J3.Kj733wNLHEdy0Ysg5kozWaRuzZlst4-1652126865-0-AQtNNxeBTjN2lkUYK97xA6X4eX7MEPk%2FADzWWzv1gHwG%2BqeOubyrpDGjJZV9GE8NeQ3DBb%2FfexWVF68s8L6NJNY%3D; __cfruid=0996b959b89a10c4e9bc13e9e4551053b156e488-1652126865; _cfuvid=ZkBPrUMvGRn1e_f8228ZVmhD9zs.t7iY1LMd.cSZLvA-1652126865994-0-604800000",
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0",
            'Accept': "*/*",
            'Accept-Language': "en-GB,en;q=0.5",
            'Referer': "https://quizlet.com/697661088/autosaved",
            'CS-Token': self.cookies.get('qtkn'),
            'Content-Type': "application/json",
            'Origin': "https://quizlet.com",
            'Connection': "keep-alive",
            'Cookie': cookie,
            'Sec-Fetch-Dest': "empty",
            'Sec-Fetch-Mode': "cors",
            'Sec-Fetch-Site': "same-origin",
            'Pragma': "no-cache",
            'Cache-Control': "no-cache",
            'TE': "trailers"
            }

        response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

        print(response.text)