import requests
from pprint import pprint

class Set():
    def __init__(self, s, cookies):
        self.s = s
        self.qtkn = cookies['qtkn']
        self.app_session_id = cookies['app_session_id']
        self.qlts = cookies['qlts']
    def publish(self, title):
        url = "https://quizlet.com/webapi/3.2/terms/save"

        querystring = {"_method":"PUT"}

        payload = "{\"data\":[{\"id\":697661088,\"title\":\"Test2\"}],\"requestId\":\"1652038877870:set:op-seq-0\"}"
        headers = {
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0",
            'Accept': "*/*",
            'Accept-Language': "en-GB,en;q=0.5",
            'Referer': "https://quizlet.com/697661088/autosaved",
            'CS-Token': "yXu7UwHSxaWs2DYNJQFGaz",
            'Content-Type': "application/json",
            'Origin': "https://quizlet.com",
            'Connection': "keep-alive",
            'Cookie': "afUserId=7a4e7c7f-36c6-45e6-84e6-dfa441cf76b1-p; qi5=5062eawwbmyn%3AWqKY4uHKxDgUuF1QqpxA; qtkn=yXu7UwHSxaWs2DYNJQFGaz; fs=rbkuij; akv=%7B%7D; __cfruid=d1490a125fe1eb4997733bcf4fa237eb87402a6c-1652039006; _cfuvid=5P0RMbK8sS8RFz9cgp7Vx2tloAV6mMMr8G1YpXZQ3D4-1652039006364-0-604800000; _gcl_au=1.1.1553204724.1652035066; session_landing_page=Login%2Fshow; qmeasure__persistence=%7B%2217%22%3A%2200100000%22%7D; _scid=2b9382fe-a824-45e3-b399-b0b9fc653553; OptanonConsent=isGpcEnabled=0&datestamp=Sun+May+08+2022+20%3A41%3A19+GMT%2B0100+(British+Summer+Time)&version=6.34.0&isIABGlobal=false&hosts=&consentId=d55f698a-a934-448c-84f2-e4f3cd9ef7e6&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0004%3A1%2CN01%3A1%2CSTACK42%3A1&geolocation=GB%3BENG&AwaitingReconsent=false; AF_SYNC=1652035068590; OptanonAlertBoxClosed=2022-05-08T18:38:30.167Z; eupubconsent-v2=CPYpcNgPYpcNgAcABBENCOCgAP_AAH_AACiQIutf_X__b3_j-_5_f_t0eY1P9_7__-0zjhfdt-8N3f_X_L8X42M7vF36pq4KuR4Eu3LBIQdlHOHcTUmw6okVrzPsbk2cr7NKJ7PEmnMbO2dYGH9_n93TuZKY7_____7z_v-v_v____f_7-3f3__5_3---_e_V_99zbn9_____9nP___9v-_9________4IsgEmGpeQBdmWODJtGkUKIEYVhIdQKACigGFoisIHVwU7K4CfUELABAKkJwIgQYgowYBAAIJAEhEQEgB4IBEARAIAAQAKgEIACNgEFgBYGAQACgGhYgRQBCBIQZEBEcpgQFSJRQT2ViCUHexphCHWeBFAo_oqEBGskYLAyEhYOY4AkBLxZIHmKF8gBGCAAA.f_gAD_gAAAAA; embedded-consent=Sun, 08 May 2022 18:38:30 GMT; _ga=GA1.2.1409053532.1652035111; _gid=GA1.2.1263945059.1652035111; _fbp=fb.1.1652035110784.1285122343; qlts=1_fNANLSAtdWlcfhC8uq3FjfVf7dE.DNDJ0vraXnUR2I.3rFuz3-Qc3QG9ObCv0yUAutfM9Pcdi4tYLg; ab.storage.userId.6f8c2b67-8bd5-42f6-9c5f-571d9701f693=%7B%22g%22%3A%22256998883%22%2C%22c%22%3A1652035117041%2C%22l%22%3A1652038877985%7D; ab.storage.sessionId.6f8c2b67-8bd5-42f6-9c5f-571d9701f693=%7B%22g%22%3A%2247604d99-d70e-1a4e-e2c9-8c89a5355c85%22%2C%22e%22%3A1652040677984%2C%22c%22%3A1652038877984%2C%22l%22%3A1652038877984%7D; ab.storage.deviceId.6f8c2b67-8bd5-42f6-9c5f-571d9701f693=%7B%22g%22%3A%224724ea93-0c85-5942-61ca-cbc1f1b1154a%22%2C%22c%22%3A1652035117042%2C%22l%22%3A1652038877985%7D; has_seen_logged_in_home_page_timestamp=1652035117866; __qca=P0-1697321322-1652035119680; app_session_id=4515f975-e3f5-40c5-8f67-eb57e4c9df8b; __cf_bm=zVARFlNDxDoz0cJmzqYbstzL8wG8cjpjcoNmXPSlpZM-1652039006-0-Aczjs1BbW0e27wiuVd1+GWQBGsL9GF6JDfSvVdX9PKO0BFddXXujmneQ+INbXSCLr9FPcVooU3fezKGGozsnZbQ=; disable-google-one-tap=1; _gat_UA-1203987-1=1",
            'Sec-Fetch-Dest': "empty",
            'Sec-Fetch-Mode': "cors",
            'Sec-Fetch-Site': "same-origin",
            'Pragma': "no-cache",
            'Cache-Control': "no-cache",
            'TE': "trailers"
            }
        response = self.s.request("POST", url, data=payload, headers=headers, params=querystring)
        return response.json()
        
    def edit(self, id : int, term  = None, definition = None):


        url = "https://quizlet.com/webapi/3.2/sets/save"

        querystring = {"_method":"PUT"}

        payload = "{\"data\":[{\"id\":697658995,\"title\":\"Test\"}],\"requestId\":\"1652035673597:set:op-seq-3\"}"
        headers = {
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0",
            'Accept': "*/*",
            'Accept-Language': "en-GB,en;q=0.5",
            'Referer': "https://quizlet.com/create-set",
            'CS-Token': "yXu7UwHSxaWs2DYNJQFGaz",
            'Content-Type': "application/json",
            'Origin': "https://quizlet.com",
            'Connection': "keep-alive",
            'Cookie': "afUserId=7a4e7c7f-36c6-45e6-84e6-dfa441cf76b1-p qi5=5062eawwbmyn%3AWqKY4uHKxDgUuF1QqpxA qtkn=yXu7UwHSxaWs2DYNJQFGaz fs=rbkuij app_session_id=b2f6bcd9-2e2c-4a73-beb4-1d42574376c4 akv=%7B%7D __cf_bm=TBdhQdd1EILyQg0Xh0Lfg5zfwWhiyQMSM0FMcPykcKs-1652036098-0-Acz3f7AmbOdThYifMDK3odhZIh/bRvzpJKn1Jy2XmwJDphWTpVBFTkt7leX7crkkn4QtJ9ND82l4OylZr4ARYxk= __cfruid=bebf96ae6854afbff7ba10d818bb0984a8e92f29-1652035195 _cfuvid=5GMQmciCdhKPEcU3yyjyg1nIXPyGwcT4JwEV0XG.8EE-1652035195619-0-604800000; _gcl_au=1.1.1553204724.1652035066; session_landing_page=Login%2Fshow; qmeasure__persistence=%7B%2217%22%3A%2200100000%22%7D; hide-fb-button=0; _scid=2b9382fe-a824-45e3-b399-b0b9fc653553; OptanonConsent=isGpcEnabled=0&datestamp=Sun+May+08+2022+19%3A47%3A55+GMT%2B0100+(British+Summer+Time)&version=6.34.0&isIABGlobal=false&hosts=&consentId=d55f698a-a934-448c-84f2-e4f3cd9ef7e6&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0004%3A1%2CN01%3A1%2CSTACK42%3A1&geolocation=GB%3BENG&AwaitingReconsent=false; AF_SYNC=1652035068590; OptanonAlertBoxClosed=2022-05-08T18:38:30.167Z; eupubconsent-v2=CPYpcNgPYpcNgAcABBENCOCgAP_AAH_AACiQIutf_X__b3_j-_5_f_t0eY1P9_7__-0zjhfdt-8N3f_X_L8X42M7vF36pq4KuR4Eu3LBIQdlHOHcTUmw6okVrzPsbk2cr7NKJ7PEmnMbO2dYGH9_n93TuZKY7_____7z_v-v_v____f_7-3f3__5_3---_e_V_99zbn9_____9nP___9v-_9________4IsgEmGpeQBdmWODJtGkUKIEYVhIdQKACigGFoisIHVwU7K4CfUELABAKkJwIgQYgowYBAAIJAEhEQEgB4IBEARAIAAQAKgEIACNgEFgBYGAQACgGhYgRQBCBIQZEBEcpgQFSJRQT2ViCUHexphCHWeBFAo_oqEBGskYLAyEhYOY4AkBLxZIHmKF8gBGCAAA.f_gAD_gAAAAA; embedded-consent=Sun, 08 May 2022 18:38:30 GMT; _ga=GA1.2.1409053532.1652035111; _gid=GA1.2.1263945059.1652035111; _fbp=fb.1.1652035110784.1285122343; qlts=1_fNANLSAtdWlcfhC8uq3FjfVf7dE.DNDJ0vraXnUR2I.3rFuz3-Qc3QG9ObCv0yUAutfM9Pcdi4tYLg; ab.storage.userId.6f8c2b67-8bd5-42f6-9c5f-571d9701f693=%7B%22g%22%3A%22256998883%22%2C%22c%22%3A1652035117041%2C%22l%22%3A1652035117042%7D; ab.storage.sessionId.6f8c2b67-8bd5-42f6-9c5f-571d9701f693=%7B%22g%22%3A%227bece695-bf61-0069-7e34-595290c64631%22%2C%22e%22%3A1652037473834%2C%22c%22%3A1652035117041%2C%22l%22%3A1652035673834%7D; ab.storage.deviceId.6f8c2b67-8bd5-42f6-9c5f-571d9701f693=%7B%22g%22%3A%224724ea93-0c85-5942-61ca-cbc1f1b1154a%22%2C%22c%22%3A1652035117042%2C%22l%22%3A1652035117042%7D; has_seen_logged_in_home_page_timestamp=1652035117866; achievements_notification=%7B%7D; __qca=P0-1697321322-1652035119680",
            'Sec-Fetch-Dest': "empty",
            'Sec-Fetch-Mode': "cors",
            'Sec-Fetch-Site': "same-origin",
            'Pragma': "no-cache",
            'Cache-Control': "no-cache"
            }

        response = self.s.request("POST", url, data=payload, headers=headers, params=querystring)

        return response.json()
