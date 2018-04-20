# -*- coding: UTF-8 -*-



import requests
from bs4 import BeautifulSoup
import sys

send_headers={
'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
'Accept-Encoding':'gzip, deflate, sdch',
'Accept-Language':'zh-CN,zh;q=0.8',
'Connection':'keep-alive',
'Cookie':'SCB_SESSION_ID=tgs0bbvqka33qoyimufmp0hl; BIGipServerpool_gzbysrc.gzpi.cn=2223181996.20480.0000; BIGipServerpool_hrssgz.gov.cn=159453356.20480.0000',
'Host':'www.hrssgz.gov.cn',
'Referer':'http://www.hrssgz.gov.cn',
'Upgrade-Insecure-Requests':'1',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36'
}

data={
'__VIEWSTATE':'/wEPDwUKMTU4MTkzNDAwOA9kFgICAQ9kFgQCAQ8QZBAVAg0tLeivt+mAieaLqS0tBDIwMTgVAgAEMjAxOBQrAwJnZ2RkAgsPPCsACwEADxYOHghEYXRhS2V5cxYBBSAzYmZiNDUzOTA5Zjg0ZGE5YTg4ZTkxZDc1ZmMzYmFmYR4QQ3VycmVudFBhZ2VJbmRleGYeEFZpcnR1YWxJdGVtQ291bnQCAR4IUGFnZVNpemUCCh4LXyFJdGVtQ291bnQCAR4VXyFEYXRhU291cmNlSXRlbUNvdW50AgEeCVBhZ2VDb3VudAIBZBYCZg9kFgICAg9kFgZmDw8WAh4EVGV4dAUJ5p2c5bCP6Z2eZGQCAQ8PFgIfBwUe5bm/5bee6aOe54m554mp5rWB5pyJ6ZmQ5YWs5Y+4ZGQCAg8PFgIfBwUKMjAxNy0xMi0yOWRkZAt/gZ5d8H6CN4bdFXEzZeoWFTqw5xJVttgYEEjhXnh3',
'__VIEWSTATEGENERATOR':'5370E590',
'DDApplyYear':'',
'TxtCorpName':'',
'TxtName':'段毅祥',
'TxtIDCard':'',
'BtnSearch':'查 询'
}

url='http://www.hrssgz.gov.cn/vsgzpiapp01/GZPI/Gateway/QueryPersonIntroduce.aspx'
response = requests.post(headers=send_headers,url=url,data=data)  # 向百度服务器发送请求

# if response.status_code == 200:  # 2xx表示成功，3xx表示你应该去另一个地址，4xx表示你错了，5xx表示服务器错了
#     print(response.text)
# else:
#     print("出错了")
# print(sys.getdefaultencoding())

soup = BeautifulSoup(response.text,'html.parser')

print soup.title

# print soup.find(id="ListItem")

tables = soup.find("table", {"class" : "listtable"})

tables1= tables.find("tr", {"class" : "ListItem"})

# 第二个class为even的，是我们所需要的
print tables1

