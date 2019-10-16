# -*-coding:utf-8-*-
import time
time_now = input("请输入开始时间:")
s,f,m = (int(i) for i in  time_now.split(":"))

while True:
    m += 1
    if m == 60:
        f += 1
        m =0
        if f == 60:
            s += 1
            f = 00
            if s == 24:
                s = 0
    print("\r当前时间为：%.2d时%.2d分%.2d秒"%(s,f,m),end='')
    time.sleep(1)

