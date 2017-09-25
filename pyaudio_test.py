#!/usr/bin/env python2
# -*- coding: utf-8-*-

# 引入库
import pyaudio
import wave

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



# 停止数据流（）
stream.stop_stream()
stream.close()

# 关闭 PyAudio
p.terminate()