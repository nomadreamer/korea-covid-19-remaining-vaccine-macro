#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
import json
import urllib3
import os
import time
import datetime
urllib3.disable_warnings()

print("사각형 모양으로 백신범위를 지정한 뒤, 해당 범위 안에 있는 백신을 조회해서 남은 백신이 있으면 Chrome 브라우저를 엽니다.")
topx = input("사각형의 위쪽 좌측 x값을 넣어주세요 : ")
topy = input("사각형의 위쪽 좌측 y값을 넣어주세요 : ")
botx = input("사각형의 아래쪽 우측 x값을 넣어주세요 : ")
boty = input("사각형의 아래쪽 우측 y값을 넣어주세요 : ")
APIURL = 'https://vaccine-map.kakao.com/api/v2/vaccine/left_count_by_coords'
APIdata = '{"bottomRight":{"x":' + botx + ',"y":' + boty + '},"onlyLeft":false,"order":"latitude","topLeft":{"x":' + topx + ',"y":' + topy + '}}'
print(APIdata)
headers = {
    "Host": "vaccine-map.kakao.com",
    "Connection": "keep-alive",
    "Origin": "https://vaccine-map.kakao.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.52 Safari/536.5",
    "Content-Type": "application/json",
    "Accept": "*/*",
    "Referer": "https://vaccine-map.kakao.com/",
    "Accept-Encoding": "gzip,deflate,sdch",
    "Accept-Language": "fr-FR,fr;q=0.8,en-US;q=0.6,en;q=0.4",
    "Accept-Charset": "ISO-8859-1,utf-8;q=0.7,*;q=0.3"
}

done = False
while done == False:
    time.sleep(1)
    response = requests.post(APIURL, data=APIdata, headers=headers, verify=False)

    received_API_status_code = response.status_code
    received_API_data = response.text

    print(received_API_data)
    print(datetime.datetime.now())

    jsonloaded = json.loads(received_API_data)
    jsonData = jsonloaded["organizations"]
    found = False
    for x in jsonData:
        if x.get('status') == "AVAILABLE" or x.get('leftCounts') != 0:
            found = x
            done = True
            break
        # keys = x.keys()
        # print(keys)
        # values = x.values()
        # print(values)


print("--- found")
print("name: " + found.get('orgName'))
print("leftCounts: " + found.get('leftCounts'))
orgCdCode = x.get('orgCode')

os.system('/usr/bin/open -a "/Applications/Google Chrome.app" "https://v-search.nid.naver.com/reservation/standby?orgCd=' + orgCdCode + '"')