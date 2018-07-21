#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import csv
import json

DOWNLOAD_URL = "https://www.lagou.com/jobs/positionAjax.json"


def get_content(url):
    headers = {
        # "Host": "www.lagou.com",
        "Cookie": "JSESSIONID=ABAAABAAADEAAFI07E4C7E0434F302DB1132156CD288A0D; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1531370343; _ga=GA1.2.940804611.1531370343; user_trace_token=20180712123902-803fecdd-858d-11e8-922f-525400f775ce; LGUID=20180712123902-803ff116-858d-11e8-922f-525400f775ce; _gid=GA1.2.483121266.1531370343; X_HTTP_TOKEN=687ac1a1eac5585bb995751c67f82ef8; _putrc=D8B49521DC89ED51123F89F2B170EADC; login=true; unick=%E6%8B%89%E5%8B%BE%E7%94%A8%E6%88%B72116; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=0; gate_login_token=0dd64357f1e62833c7137d31c0df981f20cfd4102ac58a4bd280f2357351ebce; index_location_city=%E5%85%A8%E5%9B%BD; TG-TRACK-CODE=search_code; LGSID=20180712202436-8a0a9ffe-85ce-11e8-9dd2-5254005c3644; PRE_UTM=; PRE_HOST=; PRE_SITE=https%3A%2F%2Fwww.lagou.com%2F; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Fjobs%2Flist_python%3FlabelWords%3D%26fromSearch%3Dtrue%26suginput%3D; SEARCH_ID=9521fc494d28463182b1d8f85c95c72e; LGRID=20180712204505-669a83ec-85d1-11e8-98da-525400f775ce; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1531399506",
        # "Origin": "https://www.lagou.com",
        "Referer": "https://www.lagou.com/jobs/list_Python?px=default&city=%E5%85%A8%E5%9B%BD",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36"
    }
    page = 1
    result_list = []
    while True:
        data = {'first': True, 'pn': page, 'kd': '大数据'}
        result = (requests.post(
            url, headers=headers, data=data).content).decode('utf-8')
        json_str = json.loads(result)
        print(result)
        if json_str['content']['positionResult']['resultSize'] <= 0:
            write_csv(result_list)
            break
        for json_item in json_str['content']['positionResult']['result']:
            item = [
                json_item['companyFullName'], json_item['companyShortName'],
                json_item['district'], json_item['education'],
                json_item['positionName'], json_item['salary'],
                json_item['workYear']
            ]
            result_list.append(item)
        page += 1


def write_csv(list):
    with open('./lagou.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(list)


if __name__ == '__main__':
    get_content(DOWNLOAD_URL)
