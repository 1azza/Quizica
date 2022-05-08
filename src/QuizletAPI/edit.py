import requests
from pprint import pprint
url = "https://quizlet.com/webapi/3.2/sets/save"

querystring = {"_method":"PUT"}

payload = "{\n\t\"data\": [\n\t\t{\n\t\t\t\"id\": 697562912,\n\t\t\t\"title\": \"NIce\"\n\t\t}\n\t],\n\t\"requestId\": \"1652013416691:set:op-seq-0\"\n}"
headers = {
    'cookie': "qlts=1_5lT5gInF08iRs6AcZQLQE2bYSAMHx2e.5DeUHH44IvgMTE9iIsp5imY8qRHvKTzn9qKHYnMBtCwCjw; app_session_id=0a7ad30e-656d-49fc-ae26-7732337c7179",
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0",
    'Accept': "*/*",
    'Accept-Language': "en-GB,en;q=0.5",
    'Referer': "https://quizlet.com/697562912/autosaved",
    'CS-Token': "EJBazGvKbjqC2Z87DTshTJ",
    'Content-Type': "application/json",
    'Origin': "https://quizlet.com",
    'Connection': "keep-alive",
    'Cookie': "afUserId=7a4e7c7f-36c6-45e6-84e6-dfa441cf76b1-p; qi5=d5a0x5ry4dte%3AI5-OC9Ke-mytK.N3FUSK; qtkn=EJBazGvKbjqC2Z87DTshTJ; fs=rbkd9n; app_session_id=0a7ad30e-656d-49fc-ae26-7732337c7179; akv=%7B%7D; __cf_bm=0knjC1PYQ9.MoNVAqV.QfK9yoF0CNae8eyCBZNMKzfM-1652012843-0-Aa39zbkaOa4FHC5+5iIHjnICwPhlk54nwdus2D9qr+ATaxK5Oo01wGdF39OfIyswrs5JXfaF1Z3eXmsyP5CugZI=; __cfruid=ae7fcbfcd1fa64145113e7c33d1552f6b4f147e7-1652012843; _cfuvid=QhkSO5OBt5j5CcdgcO8mRE9AT83OjjjR1oKPf1FjjLI-1652012843783-0-604800000; session_landing_page=Login%2Fshow; _gcl_au=1.1.184965443.1652012713; OptanonConsent=isGpcEnabled=0&datestamp=Sun+May+08+2022+13%3A36%3A58+GMT%2B0100+(British+Summer+Time)&version=6.34.0&isIABGlobal=false&hosts=&consentId=6761f8fb-8838-4643-ba15-a34fc7cee93f&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A0%2CC0004%3A0%2CN01%3A1%2CSTACK42%3A0&AwaitingReconsent=false; _scid=9a1fa242-25db-4a32-9d52-452a43486297; qmeasure__persistence=%7B%2217%22%3A%2200100000%22%7D; AF_SYNC=1652012715616; hide-fb-button=0; qlts=1_5lT5gInF08iRs6AcZQLQE2bYSAMHx2e.5DeUHH44IvgMTE9iIsp5imY8qRHvKTzn9qKHYnMBtCwCjw; ab.storage.userId.6f8c2b67-8bd5-42f6-9c5f-571d9701f693=%7B%22g%22%3A%22256998883%22%2C%22c%22%3A1652012722013%2C%22l%22%3A1652012722015%7D; ab.storage.sessionId.6f8c2b67-8bd5-42f6-9c5f-571d9701f693=%7B%22g%22%3A%22f9a4bf37-2fc1-c7f1-da80-d81eb5c1dba7%22%2C%22e%22%3A1652015216811%2C%22c%22%3A1652012722014%2C%22l%22%3A1652013416811%7D; ab.storage.deviceId.6f8c2b67-8bd5-42f6-9c5f-571d9701f693=%7B%22g%22%3A%22ea1d3f0e-67d9-2db9-0257-dd1bd62d8377%22%2C%22c%22%3A1652012722015%2C%22l%22%3A1652012722015%7D; has_seen_logged_in_home_page_timestamp=1652012722830; achievements_notification=%7B%7D; disable-google-one-tap=1",
    'Sec-Fetch-Dest': "empty",
    'Sec-Fetch-Mode': "cors",
    'Sec-Fetch-Site': "same-origin",
    'Pragma': "no-cache",
    'Cache-Control': "no-cache",
    'TE': "trailers"
    }

response = requests.request("PUT", url, data=payload, headers=headers, params=querystring)

pprint(response.json())