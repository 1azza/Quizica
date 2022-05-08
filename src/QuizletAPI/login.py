import requests
from pprint import pprint
url = "https://quizlet.com/login"

querystring = {"redir":"https://quizlet.com/latest"}

payload = {"password":"Larry1102","username":"larryrennoldson"}
headers = {
    'cookie': "app_session_id=0a7ad30e-656d-49fc-ae26-7732337c7179; akv=%257B%257D; qlts=1_yUpdtBvi3kb89.NS.mXC8d.3d9ATfUs.yec9ZFNwxpteFA3iaWMaKf5zu1weaFeL5nh5zrfMdGH4hw; qtkn=fxvFGhATkbttsPjSWXnbZV; ts2ce=eyJldmVudCI6ImFmdGVyLWxvZ2luIn0%253D",
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0",
    'Accept': "application/json",
    'Accept-Language': "en-GB,en;q=0.5",
    'Referer': "https://quizlet.com/login?redir=https://quizlet.com/latest",
    'CS-Token': "zNRM2JMPRDNq4kP3Zktp2f",
    'x-requested-with': "XMLHttpRequest",
    'Content-Type': "application/json",
    'Origin': "https://quizlet.com",
    'Connection': "keep-alive",
    'Cookie': "afUserId=7a4e7c7f-36c6-45e6-84e6-dfa441cf76b1-p; qi5=d5a0x5ry4dte%3AI5-OC9Ke-mytK.N3FUSK; qtkn=zNRM2JMPRDNq4kP3Zktp2f; fs=rbkd9n; app_session_id=0a7ad30e-656d-49fc-ae26-7732337c7179; akv=%7B%7D; __cf_bm=0knjC1PYQ9.MoNVAqV.QfK9yoF0CNae8eyCBZNMKzfM-1652012843-0-Aa39zbkaOa4FHC5+5iIHjnICwPhlk54nwdus2D9qr+ATaxK5Oo01wGdF39OfIyswrs5JXfaF1Z3eXmsyP5CugZI=; __cfruid=ae7fcbfcd1fa64145113e7c33d1552f6b4f147e7-1652012843; _cfuvid=QhkSO5OBt5j5CcdgcO8mRE9AT83OjjjR1oKPf1FjjLI-1652012843783-0-604800000; disable-google-one-tap=1; session_landing_page=Login%2Fshow; _gcl_au=1.1.184965443.1652012713; OptanonConsent=isGpcEnabled=0&datestamp=Sun+May+08+2022+13%3A25%3A14+GMT%2B0100+(British+Summer+Time)&version=6.34.0&isIABGlobal=false&hosts=&consentId=6761f8fb-8838-4643-ba15-a34fc7cee93f&interactionCount=0&landingPath=https%3A%2F%2Fquizlet.com%2Flogin%3Fredir%3Dhttps%3A%2F%2Fquizlet.com%2Flatest&groups=C0001%3A1%2CC0002%3A0%2CC0004%3A0%2CN01%3A1%2CSTACK42%3A0; _scid=9a1fa242-25db-4a32-9d52-452a43486297; qmeasure__persistence=%7B%2217%22%3A%2200100000%22%7D; AF_SYNC=1652012715616; hide-fb-button=0",
    'Sec-Fetch-Dest': "empty",
    'Sec-Fetch-Mode': "cors",
    'Sec-Fetch-Site': "same-origin",
    'Pragma': "no-cache",
    'Cache-Control': "no-cache",
    'TE': "trailers"
    }

response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

if (response.json().get('success')) == True:
    print('Login Successful')
else:
    for i in response.json().get('errors'):
        print(i.get('message'))
