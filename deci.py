#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 常用的字母代表数字的字典
dic = {'10': 'A',
       '11': 'B',
       '12': 'C',
       '13': 'D',
       '14': 'E',
       '15': 'F'}

# 将weight进制的某一位的值对应的十进制的值算出来


def PlaceValue(nvalue, scale, digits):
    Quan = 1  # 某一位的权值,初始为1
    for i in range(1, digits + 1):
        Quan = scale * Quan
    return nvalue * Quan

# scale进制的值value转为对应10进制的值


def N_2_decimal(value, scale):
    sum = 0
    n = len(str(value))  # 数值的位数长度
    for i in range(1, n + 1):
        sum = sum + PlaceValue(int(str(value)[i - 1]), scale, n - i)
    return sum

# 10进制的值value转为对应scale进制的值


def decimal_2_N(value, scale):
    arr = []
    i = 0
    while value is not 0:
        rem = value % scale
        if rem >= 16:
            rem = "*" + str(rem) + "*"
        if rem <= 15 and rem >= 10:
            rem = dic[str(rem)]
        value = value / scale
        arr.append(rem)
        i += 1
    return arr
