# -*- coding:UTF-8 -*-

filename = 'lover dating.txt'
z = open(filename, 'a')

for ZH in range(1314):
    then= 'Row no.=%d\nPlease love me again' % (ZH+1)
    z.write(then)

z.close()
