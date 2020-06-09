# -*- coding: UTF-8 -*-


'''
for num in range(5):
for num in range(1,5):
for num in range(1,5,2):
'''
num_start = 1
num_end = 520

num_input=input('Type an end number:')
num_end=int(num_input)

sum = 0
# 自然数求和
for num in range(num_start, num_end + 1):
    sum += num

print (sum)
