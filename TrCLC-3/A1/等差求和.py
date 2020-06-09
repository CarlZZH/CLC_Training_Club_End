# -*- coding: UTF-8 -*-
num_start = 1
loops = 5
ap_step = 5

sum = 0
y = num_start
for num in range(loops):
    sum += y
    y *= ap_step

print(sum)
