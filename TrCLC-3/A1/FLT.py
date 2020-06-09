# -*- coding: UTF-8 -*-

max_num=10

for a in range(max_num*-1,max_num):
    for b in range(max_num*-1,max_num):
        c=a*a+b*b
        if c>=0 and c<=100:
            print('found it! a=%0f b=%0f' % (a,b))
