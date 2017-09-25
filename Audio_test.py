# -*- coding: utf-8 -*-

import xiaoi.ibotcloud  #小i库
from aip import AipSpeech #百度库
# 引入播放库
import pyaudio
import wave

#小i的授权
test_key = "H1kR9wAEcxJU"
test_sec = "DlnMjTL3BU73H5srxrF9"
content = "广州天气" #以后这里放语言识别出来的信息
#百度的授权
APP_ID = '9993998'
API_KEY = 'bkEaVju6jjgSp90xlWE03RLB'
SECRET_KEY = 'xVYqqNPvpBDXh6Hpa7sUKisMbnD4SDcC'

#******************请求小i接口拿到交互的结果***********************
signature_ask = xiaoi.ibotcloud.IBotSignature(app_key=test_key,
                                              app_sec=test_sec,
                                              uri="/ask.do",
                                              http_method="POST")


params_ask = xiaoi.ibotcloud.AskParams(platform="custom",
                                       user_id="abc",
                                       url="http://nlp.xiaoi.com/ask.do",
                                       response_format="xml")

ask_session = xiaoi.ibotcloud.AskSession(signature_ask, params_ask)
ret_ask = ask_session.get_answer(content)
#小i接口返回状态码，返回结果
# print ret_ask.http_status, ret_ask.http_body

#******************请求百度接口把交互结果转化为语音文件***********************

# 初始化AipSpeech对象
aipSpeech = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

#原始语音的录音格式目前只支持评测 8k/16k 采样率 16bit 位深的单声道语音
# 读取文件
result  = aipSpeech.synthesis(ret_ask.http_body, 'zh', 1, {
    'vol': 5,
})
#把文件写到本地然后让pyaudio去读
if not isinstance(result, dict):
    with open('hehe.wav', 'wb') as f:
        f.write(result)
#
# ******************请求百度接口生成的语音文件用PyAudio读出来***********************
# 定义数据流块
chunk = 1024
url=r"G:\python\python27\hehe.wav"
# 只读方式打开wav文件
f = wave.open(url, "rb")

p = pyaudio.PyAudio()

# 打开数据流
stream = p.open(format=p.get_format_from_width(f.getsampwidth()),
                channels=f.getnchannels(),
                rate=f.getframerate(),
                output=True)

print p.get_format_from_width(f.getsampwidth())
print f.getnchannels()
print f.getframerate()
# 读取数据
data = f.readframes(chunk)

# 播放
while data != "":
    stream.write(data)
    data = f.readframes(chunk)



# 停止数据流
stream.stop_stream()
stream.close()

# 关闭 PyAudio
p.terminate()
