# -*- coding:UTF-8 -*-


def pnt_cut_line(sn):
    'Desc:Print a cutting line for me'
    print('/n--------No(%d)cutting line--------' % (sn))
    return


def double_list(input_list):
    'double all elements of a list'
    list_lenth = len(input_list)
    for idx in range(list_lenth):
    return


def fill_list(input_output_list):
    'Fill sth. into an empty list'
    for element_data in range(10):
        input_output_list.append(element_data)
    return


def cal_triangle_area(a, b, c):
    # 海伦公式
    p = (a + b + c) / 2
    area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    return area
