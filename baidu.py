#!/usr/bin/env python2
# -*- coding: utf-8-*-

# 引入NLP SDK
from aip import AipNlp
import json
# 定义常量
APP_ID = '9993998'
API_KEY = 'bkEaVju6jjgSp90xlWE03RLB'
SECRET_KEY = 'xVYqqNPvpBDXh6Hpa7sUKisMbnD4SDcC'

# 初始化AipNlp对象
aipNlp = AipNlp(APP_ID, API_KEY, SECRET_KEY)


# result = aipNlp.lexer('学习雷锋好榜样忠于革命忠于党')
# result1 = aipNlp.sentimentClassify('你是一个大傻逼')
# result2 = aipNlp.dnnlm('飞特是一个优秀的物流公司')
# result3 = aipNlp.simnet('飞特是个国际物流公司', '发货去美国找飞特')

# 定义参数变量 1:酒店，2:KTV ，3:丽人，4:美食（默认值），5:旅游，6:健康7:教育，8:商业，9:房产，10:汽车，11:生活，12:购物, 13: 3C
# 汽车分类
option = {'type': 1}

# 调用情感观点抽取接口（）
result4 = aipNlp.commentTag('如家很便宜', option)


# print json.dumps(result, ensure_ascii=False, encoding='UTF-8')
# print json.dumps(result1, ensure_ascii=False, encoding='UTF-8')
# print json.dumps(result2, ensure_ascii=False, encoding='UTF-8')
# print json.dumps(result3, ensure_ascii=False, encoding='UTF-8')
print json.dumps(result4, ensure_ascii=False, encoding='UTF-8')