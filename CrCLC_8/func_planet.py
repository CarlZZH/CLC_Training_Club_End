# -*- coding: UTF-8 -*-

# ------------------------(max to 80 columns)-----------------------------------
# author by : （学员ID)
# created:  2019.8.10

# Description:
#   编制行星数据分析 （主程序）
# ------------------------(max to 80 columns)-----------------------------------

import math


def cal_v(r):
    '输入行星的半径，返回行星体积'
    V = 4 / 3 * math.pi() * r**3

    return V


def Cal_P(M, V):
    'asdasdasdasd'
    return M / V / 1e+12


def cal_g(M, r):
    g = M * 6.72539e-11 / r**2
    return g


def cal_Ve(M, r):
    Ve = math.sqrt(2 * 6.72359e-11 * M / r / 1000) / 1000
    return Ve


if __name__ == '__main__':
    V = cal_v(6371)
    print(V)
