#!/usr/bin/env python3
#a = range(23,32)
sum = 0
N = 10
count = 0
print("请输入10个数字:")
while count < N:
    number = float(input())
    sum  = sum + number
    count = count + 1
average = sum / N 

#for i in a:
#    sum = sum + i

print("N = {}, sum = {}".format(N, sum))
print("Average = {:.2f}".format(average))
