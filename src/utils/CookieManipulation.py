def headerToDict(header):
    cookies = header.split(';')
    x = {}
    for i in cookies:
        print(i)
        i = i.split('=')
        try:
            x[i[0]] = i[1]
        except:
            continue
    return f'\n\n{x}'
def dictToHeader(dic):
    dic = dict(dic)
    cookie_string = "; ".join([str(x)+"="+str(y) for x,y in dic.items()])
    return cookie_string
def main():
# cookies = """{'session_landing_page': 'StudyFeed%2FlatestActivity', ' app_session_id': 'cbed39b0-b0bc-4cd6-abaa-bdbc27deb66c', ' qi5': '2c153zlsjte6%3AqKhONeOC-i4SczMQhLx9', ' qtkn': '5mewGpYX6MRgNkHKeE4Qhb', ' fs': 'rbmif8', ' __cf_bm': '3oz9Nytm8wIsE3Bd7FOeQdgxTfNtX8h4NGM.CMp9350-1652112836-0-ARv4zj1mUrTm8hEUkGrvffXK3qOleRLMH+oi5/dRyMCPVx4az9wmH0H08PDo+w7oD7f3IS33f3twXUUfLILhNwI', ' __cfruid': 'e3abcc0b1c44a831ae72b9cc6cb6aed14c2259f6-1652112836', ' _cfuvid': 'Sv.2zbk7m2H1d8nisTyhnmPgUfrDrL9SE01PSgBqeMY-1652112836196-0-604800000', ' afUserId': '7a4e7c7f-36c6-45e6-84e6-dfa441cf76b1-p', ' akv': '%7B%7D', ' disable-google-one-tap': '1', ' _gcl_au': '1.1.1422438553.1652112707', ' OptanonConsent': 'isGpcEnabled', ' _scid': 'a19f8806-d250-4600-80d3-ff7a8149ee23', ' hide-fb-button': '0', ' qmeasure__persistence': '%7B%2217%22%3A%2200100000%22%7D', ' AF_SYNC': '1652112708127'}"""
    cookies = input('Enter your cookies: ')
    print(f'\n\n{headerToDict(cookies)}')
if __name__ == '__main__':
    main()
