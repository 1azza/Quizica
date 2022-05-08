import requests
from pprint import pprint
class Set():
    def __init__(self, cookies):
        self.qtkn = cookies['qtkn']
        self.app_session_id = cookies['app_session_id']
        self.qlts = cookies['qlts']
    def create(self, title):
        pass
    def edit(self, id : int, term  = None, definition = None):

        url = "https://quizlet.com/webapi/3.2/sets/save"

        querystring = {"_method":"PUT"}

        payload = "{\n\t\"data\": [\n\t\t{\n\t\t\t\"id\": 697562912,\n\t\t\t\"title\": \"Metalssdf\"\n\t\t}\n\t],\n\t\"requestId\": \"1652013416691:set:op-seq-0\"\n}"
        headers = {
            'cookie': "qlts=1_5lT5gInF08iRs6AcZQLQE2bYSAMHx2e.5DeUHH44IvgMTE9iIsp5imY8qRHvKTzn9qKHYnMBtCwCjw; app_session_id=0a7ad30e-656d-49fc-ae26-7732337c7179; __cf_bm=iiz0pGQN94EZQmddZjNx4.6x_1_1VVG.Lpl6_G9CCms-1652026435-0-AWBCPZzhWuVek4CH5Ri8BHOuAoClUFJSursCeZsbquZOwdjQ6jGrBwC/rnvpqLxlnhG+Vd1UxcsJLi9g5eoYVT0=",
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0",
            'Accept': "*/*",
            'Accept-Language': "en-GB,en;q=0.5",
            'Referer': "https://quizlet.com/697562912/autosaved",
            'CS-Token': "EJBazGvKbjqC2Z87DTshTJ",
            'Content-Type': "application/json",
            'Origin': "https://quizlet.com",
            'Connection': "keep-alive",
            'Cookie': "afUserId=7a4e7c7f-36c6-45e6-84e6-dfa441cf76b1-p; session_landing_page=Sets%2Fshow; app_session_id=7bbf2588-9e68-4dd7-9e7e-709f9ac66549; qi5=n49tz3xzrzag%3AVgrt4Td8p-xirpBaEQf8; qtkn=v3T4x7Sq9PazhcVajSbJGw; fs=rbkkbm; akv=%7B%7D; qmeasure__persistence=%7B%2210%22%3A%2200000001%22%2C%2217%22%3A%2200101000%22%2C%2213%22%3A%2200010000%22%7D; __cf_bm=Cm_9Q6nRj.kvuzXj19ngMTDRDg99TM3LfdzKNrJ3UwE-1652021986-0-ASQ0+tGosbMeKi4PCCwzsnwbzwppXOLLv+ZjVBoblPoR5zK2f9I/w/owDTIJroyl++kl4xtetGBxkl7O7nRB/yI=; __cfruid=ab9693d56db2561bb2d44056d03daba82e5a7165-1652021986; _cfuvid=4sMlVMkyjW09Qb8w46TcmUeeavGlevViHdm1C1iQW8Q-1652021986427-0-604800000; _gcl_au=1.1.1321380596.1652021857; OptanonConsent=isGpcEnabled=0&datestamp=Sun+May+08+2022+15%3A57%3A37+GMT%2B0100+(British+Summer+Time)&version=6.34.0&isIABGlobal=false&hosts=&consentId=e40eb15a-acc7-4902-afe0-ddaa0a461c78&interactionCount=0&landingPath=https%3A%2F%2Fquizlet.com%2Fgb%2F697562912%2Fmetalssdf-flash-cards%2F&groups=C0001%3A1%2CC0002%3A0%2CC0004%3A0%2CN01%3A1%2CSTACK42%3A0; hide-fb-button=0; _lr_geo_location=GB; AF_SYNC=1652021858129",

            'Sec-Fetch-Dest': "empty",
            'Sec-Fetch-Mode': "cors",
            'Sec-Fetch-Site': "same-origin",
            'Pragma': "no-cache",
            'Cache-Control': "no-cache",
            'TE': "trailers"
            }

        response = requests.request("PUT", url, data=payload, headers=headers, params=querystring)

        print(response.text)