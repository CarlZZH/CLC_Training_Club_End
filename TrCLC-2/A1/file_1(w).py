# -*- coding:UTF-8 -*-

filename = 'lover dating.txt'
z = open(filename, 'w')

for h in range(520):
    data = 'Row no.= %02d Hello LZH\n' % (h+1)
    z.write(data)

z.close()
