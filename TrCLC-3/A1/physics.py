# -*- coding: UTF-8 -*-

H0 = 100
times = 20
rate = 0.5

sum = H0
Hn = H0 * rate
for n in range(2, times + 1):
    sum += 2 * Hn
    print('No.%2d - Hn=%7.4f sum=%7.4f' % (n, Hn, sum)) 
    Hn *= rate

print(sum)
