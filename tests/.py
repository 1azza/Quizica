import requests
from CookieManipulation import headerToDict, dictToHeader
url = "https://quizlet.com/login"

cookies = {'afUserId': '7a4e7c7f-36c6-45e6-84e6-dfa441cf76b1-p',
           ' qi5': '1g2ur5no6lccf%3AnFE2qJ6P0Y90BFnjnXFO',
           ' qtkn': 'G2FdR2FnEsVKpwtTMGuG2q',
           ' fs': 'rbmngy', 
           ' app_session_id': 'b21ca688-d008-42af-900f-32eca19e164f',
           ' __cf_bm': '2mykJ5OkleKBXIlGCRfOewouR2NKQkZGcN8f6fvUU_Y-1652124680-0-ASm/Qjm8TsKOLF95Pzxu+94YHJQHxEIuw4+VgHzpXu8NP+uWq8hksineWlZPeUPXfMd2T6qlO+SQ97a5VFQQ5qM=',
           }
cookies = dictToHeader(cookies)
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

