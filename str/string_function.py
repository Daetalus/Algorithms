#!/usr/bin/env python
# -*- coding:utf-8 -*-
from __future__ import division
from __future__ import unicode_literals
from __future__ import print_function


def reverseStr(input_str, begin, end):
    # Pythonic way should be input_str[::-1]
    str_list = list(input_str)
    while begin < end:
        str_list[begin], str_list[end] = str_list[end], str_list[begin]
        begin += 1
        end -= 1
    return ''.join(str_list)

def reveseWord(input_str):
    input_str = input_str[::-1]
    str_list = input_str.split()
    for i in xrange(len(str_list)):
        str_list[i] = str_list[i][::-1]
    return ' '.join(str_list)

if __name__ == '__main__':
    test = "I am a student."
    result = reveseWord(test)
    # result = reverseStr(test, 0, len(test) - 1)
    print(result)
