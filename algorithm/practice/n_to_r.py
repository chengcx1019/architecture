#!/usr/bin/env python
# encoding: utf-8

"""
@author: changxin
@mail: chengcx1019@gmail.com
@file: n_to_r.py
@time: 2018/6/7 09:36
"""


def int_to_roman(num):
    if num is None or num < 0:
        return
    result = ''
    int_num = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    roman = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    for i in range(len(int_num)):
        if num > 0:
            if num < int_num[i]:
                continue
            while num >= int_num[i]:
                num -= int_num[i]
                result += roman[i]

    return result


def roman_to_int(roman_str):
    roman_int = {
        "M": 1000,
        "D": 500,
        "C": 100,
        "L": 50,
        "X": 10,
        "V": 5,
        "I": 1
    }
    num = 0
    for i in range(len(roman_str)):
        if roman_str[i] not in roman_int.keys():
            print("invalid char")
            return

        if i < len(roman_str) - 1:
            if roman_int[roman_str[i]] >= roman_int[roman_str[i+1]]:
                num += roman_int[roman_str[i]]
            else:
                num -= roman_int[roman_str[i]]
        else:
            num += roman_int[roman_str[i]]

    return num


if __name__ == '__main__':
    print(int_to_roman(4))
    print(roman_to_int('CMX'))