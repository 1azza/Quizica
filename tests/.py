import requests

url = "https://quizlet.com/login"

querystring = {"redir":"https://quizlet.com/gb/697562912/metalssdf-flash-cards/"}

payload = "{\"password\":\"Larry1102\",\"username\":\"larryrennoldson\"}"
headers = {
    'cookie': "app_session_id=7bbf2588-9e68-4dd7-9e7e-709f9ac66549; akv=%257B%257D; qlts=1_.Qf1scgYM62Clx5G2WN-usNYtDFiIEwR6yl5Iq4W8LIZt72h.taOxe2zBvAKO9jHDKpyo3axlEotvw; qtkn=3C6B3EERMQNGFkBhVRcZ9V; ts2ce=eyJldmVudCI6ImFmdGVyLWxvZ2luIn0%253D; __cf_bm=RE7IvH1LHPHT6H2OazdmS4A0ZW4MCBx7CG7EZY8F4VM-1652025173-0-AQpp121rRd1F3aediBQFMEy4Fxm1T9t%2FQ36pI3nJ2utlqo5mTZMWlEhV6%2BMmAplwiczbjuOxKZY0G3iqr5eLxKM%3D",
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0",
    'Accept': "application/json",
    'Accept-Language': "en-GB,en;q=0.5",
    'Referer': "https://quizlet.com/gb/697562912/metalssdf-flash-cards/",
    'CS-Token': "XHQycWDd6V4VTPGcdsta8r",
    'x-requested-with': "XMLHttpRequest",
    'Content-Type': "application/json",
    'Origin': "https://quizlet.com",
    'Connection': "keep-alive",
    'Cookie': "afUserId=7a4e7c7f-36c6-45e6-84e6-dfa441cf76b1-p; session_landing_page=Sets%2Fshow; app_session_id=7bbf2588-9e68-4dd7-9e7e-709f9ac66549; qi5=n49tz3xzrzag%3AVgrt4Td8p-xirpBaEQf8; qtkn=XHQycWDd6V4VTPGcdsta8r; fs=rbkkbm; akv=%7B%7D; qmeasure__persistence=%7B%2210%22%3A%2200000001%22%2C%2217%22%3A%2200101000%22%2C%2213%22%3A%2200010000%22%7D; __cf_bm=Cm_9Q6nRj.kvuzXj19ngMTDRDg99TM3LfdzKNrJ3UwE-1652021986-0-ASQ0+tGosbMeKi4PCCwzsnwbzwppXOLLv+ZjVBoblPoR5zK2f9I/w/owDTIJroyl++kl4xtetGBxkl7O7nRB/yI=; __cfruid=ab9693d56db2561bb2d44056d03daba82e5a7165-1652021986; _cfuvid=4sMlVMkyjW09Qb8w46TcmUeeavGlevViHdm1C1iQW8Q-1652021986427-0-604800000; _gcl_au=1.1.1321380596.1652021857; OptanonConsent=isGpcEnabled=0&datestamp=Sun+May+08+2022+15%3A57%3A37+GMT%2B0100+(British+Summer+Time)&version=6.34.0&isIABGlobal=false&hosts=&consentId=e40eb15a-acc7-4902-afe0-ddaa0a461c78&interactionCount=0&landingPath=https%3A%2F%2Fquizlet.com%2Fgb%2F697562912%2Fmetalssdf-flash-cards%2F&groups=C0001%3A1%2CC0002%3A0%2CC0004%3A0%2CN01%3A1%2CSTACK42%3A0; hide-fb-button=0; _lr_geo_location=GB; AF_SYNC=1652021858129",
    'Sec-Fetch-Dest': "empty",
    'Sec-Fetch-Mode': "cors",
    'Sec-Fetch-Site': "same-origin",
    'Pragma': "no-cache",
    'Cache-Control': "no-cache",
    'TE': "trailers"
    }

response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

print(response.text)