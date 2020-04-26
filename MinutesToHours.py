#!/usr/bin/env python3
import sys

#时间转换函数
def Hours(minute):
    #如果为负数则 raise 异常
    if minute < 0:
        raise ValueError("Input number connot be negative")
    else:
        print('{} H, {} M'.format(int(minute / 60), minute % 60))

#函数调用及异常处理
try:
    Hours(int(sys.argv[1]))
except:
    print('Parameter Error')
