import requests
import pandas as pd

sbRequests = [
    {
        'sb' : 'bovada',
        'sbUrl': 'https://www.bovada.lv/sports/football/nfl',
        'reqUrl' : 'https://www.bovada.lv/services/sports/event/coupon/events/A/description/football/nfl?marketFilterId=def&preMatchOnly=true&eventsLimit=5000&lang=en',
        'headersList' : {
            "authority": "www.bovada.lv",
            "accept": "application/json, text/plain, */*",
            "accept-language": "en-US,en;q=0.8",
            "authorization": "Bearer b06c8e8d-350d-496a-8667-946f44ffbfe2",
            "cookie": "VISITED=true; Device-Type=Desktop|false; LANG=en; AB=variant; JOINED=true; url-prefix=/; ln_grp=1; odds_format=AMERICAN; audiences=45521bdb06873bbf1674a64161dd794f; sid=b06c8e8d-350d-496a-8667-946f44ffbfe2; variant=v:1|lgn:1|dt:d|os:w|cntry:US|cur:USD|jn:1|rt:o|pb:0; JSESSIONID=9D66668B7FB83FC72876861A9D965F5F",
            "referer": "https://www.bovada.lv/",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "sec-gpc": "1",
            "traceparent": "00-577d8c13bed99c3447f97b8865b81f15-2726339375c45b90-00",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
            "x-channel": "desktop",
            "x-sport-context": "FOOT" 
        },
        'payload' : ''
    },
    # {
    #     'sb' : '',
    #     'sbUrl':'',
    #     'reqUrl': '',
    #     'headerList': {}
    # }
]

res = []

for sb in sbRequests:
    r = requests.request("GET", sb['reqUrl'], data=sb['payload'],  headers=sb['headersList'])
    data = r.json()

    for g in data[0]['events']:
        res.append(g)

            
print (len(res))


