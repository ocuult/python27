#!/usr/bin/env python2
# -*- coding: utf-8-*-

# 引入Speech SDK
from aip import AipSpeech
import json


APP_ID = '9993998'
API_KEY = 'bkEaVju6jjgSp90xlWE03RLB'
SECRET_KEY = 'xVYqqNPvpBDXh6Hpa7sUKisMbnD4SDcC'

# 初始化AipSpeech对象
aipSpeech = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

#原始语音的录音格式目前只支持评测 8k/16k 采样率 16bit 位深的单声道语音
# 读取文件
result  = aipSpeech.synthesis('你好百度', 'zh', 1, {
    'vol': 5,
})

if not isinstance(result, dict):
    with open('auido.wav', 'wb') as f:
        f.write(result)