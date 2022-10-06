import requests
from bs4 import BeautifulSoup
from pprint import pprint
import json
import time
datas = []
for page in range(1,151):
    response = requests.post(
        'https://auction.realestate.daum.net/ajax/main_list.php?addr1=%EC%84%9C%EC%9A%B8&result=99&yongdo=99&yongdo_detail=99&sort=13D',
        params={
            'addr1': '서울',
            'result': '99',
            'yongdo': '99',
            'yongdo_detail': '99',
            'sort': '13D',
        },
        data={
            'total': '1304',
            'block': page,
            'start': '',
            'next': '',
            'addr1': '서울',
            'addr2': '',
            'addr3': '',
            'bubcd': '',
            'kye': '',
            'local_num': '',
            'var_period':'',
            'result': '99',
            'var_kind': '',
            'yuchalcnt': '',
            'gamprice': '',
            'lowprice': '',
            'bdarea': '',
            'daejiarea': '',
            'ipchaltype':'',
            'bdname': '',
            'special': '',
            'addshow': '',
            'sort': '13D',
            'subMenuIdx': '1',
        },
        headers={
            'Origin': 'https://auction.realestate.daum.net',
            'Referer': 'https://auction.realestate.daum.net/v15/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
        },
    )


    # with open('./result.html', 'w', encoding="utf-8") as f:
    #          f.write(response.text)
    soup = BeautifulSoup(response.text, 'html.parser')
    trs= soup.select('#frm_myreg > table > tbody > tr')
    print('페이지',page, '/', 'tr수',len(trs))

    if len(trs) == 0:
        print(f'{page}페이지가 비었습니다 ')
        break

    
    for tr in trs:
        data= {
              '사건번호': tr.select_one('td:nth-child(1) a').get_text(),
            '물건용도': tr.select_one('td:nth-child(2) > div:nth-child(2) > a > p:nth-child(1)').get_text(),
            '소재지': tr.select_one('td:nth-child(2) > div:nth-child(2) > a > p:nth-child(2)').get_text(),
            '면적': tr.select_one('td:nth-child(2) > div:nth-child(2) > p:nth-child(2)').get_text(),
            '감정가': tr.select_one('td:nth-child(3) > div:nth-child(1) > p:nth-child(1)').get_text(),
        }
        datas.append(data)
        time.sleep(5)


with open('./code_1.json', 'w', encoding='utf-8') as f:
    f.write(json.dumps(datas, ensure_ascii=False))