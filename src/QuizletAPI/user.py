import requests
from pprint import pprint
import logging

class User():
    def __init__(self, s, username, password):
        self.s = s
        self.username = username
        self.password = password
    def login(self):
        c1 = {
        "name":'fs',
        "value":'rbkyol',
        "domain":'quizlet.com',
        }
        c2 = {
        "name":'app_session_id',
        "value":'61451c28-db09-40a4-bcdf-3cff1a087791',
        "domain":'quizlet.com',
        "path":'/',
        }
        c3 = {
        "name":'qtkn',
        "value":'smXfhHUQBvW6NTAm7avT6M',
        "domain":'quizlet.com',
        }
        c3 = {
        "name":'qi5',
        "value":'eji7q5755vvc%3AJ-Yl883ZvZL25KrIH9YV',
        "domain":'quizlet.com',
        }
        
        self.s.cookies.set(**c1)
        self.s.cookies.set(**c2)
        self.s.cookies.set(**c3)
        url = "https://el.quizlet.com/"
        payload = "{\"namespace\":\"events\",\"type\":\"page_actions\",\"event\":{\"action_name\":\"metric_check_page_header\",\"additional_info\":\"{\\\"transaction_name\\\":\\\"Login\\\\/show\\\"}\",\"client_timestamp\":1652040600.2527,\"device_category\":\"desktop\",\"request_id\":\"Aacm5aVEJzSDaRJagJGr\",\"server_timestamp\":1652040600,\"user_agent\":\"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36\"},\"dev_name\":null}"
        headers = {
            'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36"
            }
        self.s.request("POST", url, data=payload, headers=headers)
        c = self.s.cookies.get_dict()
        url = "https://quizlet.com/webapi/3.2/measure-enrollments/enroll"
        payload = "{\"testName\":\"InternationalTestPrepHoneypotPositionV2\",\"variation\":\"control\"}"
        headers = {
            'cs-token': "p3hXhfFz45UsbQnxC5UfkU",
            'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36"
            }
        self.s.request("POST", url, data=payload, headers=headers)     

        url = "https://quizlet.com/login"

        querystring = {"redir":"https://quizlet.com/en-gb"}

        payload = "{\"password\":\"Larry1102\",\"username\":\"larryrennoldson\"}"
        headers = {
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0",
            'Accept': "application/json",
            'Accept-Language': "en-GB,en;q=0.5",
            'Referer': "https://quizlet.com/en-gb",
            'CS-Token': "smXfhHUQBvW6NTAm7avT6M",
            'x-requested-with': "XMLHttpRequest",
            'Content-Type': "application/json",
            'Origin': "https://quizlet.com",
            'Connection': "keep-alive",
            'Cookie': "__cf_bm=XStI59GBF9sNA5nYqBFnHMF3T8Z9HVKMBhNvhrWFDSM-1652044651-0-AZ4t08+2gvGGuebnckoWmcfDKOxJ8M+mfvt9WUBQCZH4sIpDz2GSMbIdi2aSdBYWrx9cCvIAVoPinAqUrGgduGs=; __cfruid=370984a525eea72715c0d5987881e92d5505761f-1652044650; _cfuvid=bt3cT2Gai57tNJG_LsCJRVyI5uwGMhS6cFcWWpfHdJU-1652044650944-0-604800000; app_session_id=61451c28-db09-40a4-bcdf-3cff1a087791; fs=rbkyol; qi5=eji7q5755vvc%3AJ-Yl883ZvZL25KrIH9YV; qtkn=smXfhHUQBvW6NTAm7avT6M",
            'Sec-Fetch-Dest': "empty",
            'Sec-Fetch-Mode': "cors",
            'Sec-Fetch-Site': "same-origin",
            'Pragma': "no-cache",
            'Cache-Control': "no-cache",
            'TE': "trailers"
            }

        response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

        # cookie_string = "; ".join([str(x)+"="+str(y) for x,y in self.s.cookies.get_dict().items()])
        # print(cookie_string)
        if response.status_code == 403:
            print('Captcha blocked us')
            return
        if (response.json().get('success')) == True:
            logging.info('Login Successful')
        else:
            for i in response.json().get('errors'):
                print(i.get('message'))
        return response.cookies.get_dict()