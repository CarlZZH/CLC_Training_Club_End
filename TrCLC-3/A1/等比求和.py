# -*- coding: UTF-8 -*-
import Fraction

num_start=1
num_end=5

sum=-0
for num in range(num_start,num_end+1):
    fc=fractions.Fraction(1,num)
    sum += fc
    print('%s - %0.2f' % (fc,sum))

print(sum)
