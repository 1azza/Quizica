import requests
def getCfbm():
    url = "https://el.quizlet.com/"
    headers = {
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0",
            }
    response = requests.request("POST", url, headers=headers)
    cfbm = (response.cookies.get_dict().get('__cf_bm'))
    return cfbm