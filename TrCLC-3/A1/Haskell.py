# -*- coding: UTF-8 -*-

max_num = 10

fname = 'Haskell.txt'
f = open(fname, 'w')

for a in range(1, max_num):
    data = ''
    for b in range(1, max_num):
        c = a * b
        if b<=a:
            print('%dx%d=%d\t' % (a, b, c), end='')
            data += '%dx%d=%d\t' % (a, b, c)

    print('\n')
    data += '\n'
    f.write(data)

f.close()
