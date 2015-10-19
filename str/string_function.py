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


def atoi(str):
    # check is None first
    if not str:
        return 0

    # Second, strip str
    index = 0
    while str[index] == ' ':
        index += 1

    # Third, check sign
    positive = True
    if str[index] == '-':
        positive = False
        index += 1
    if str[index] == '+':
        index += 1

    # loop, get the result
    result = 0
    for i in xrange(index, len(str)):
        # if not a digit, break, return current result
        # Question: What about "213k"?
        # return 0 or 213?
        if not str[i].isdigit():
            break
        digit = ord(str[i]) - ord('0')
        result = result * 10 + digit
    # check overflow
    if positive:
        if result > 2147483647:
            return 2147483647
        return result
    else:
        if -result < -2147483648:
            return -2147483648
        return -result


def isPalindrome(self, s):
    start = 0
    end = len(s) - 1

    while start < end:
        while not s[start].isalnum() and start < end:
            start += 1

        while not s[end].isalnum() and start < end:
            end -= 1

        if start < end and s[start].lower() != s[end].lower():
            return False
        end -= 1
        start += 1

    return True


if __name__ == '__main__':
    test = "I am a student."
    result = reveseWord(test)
    test1 = "World"
    result = reveseWord(test1)
    # result = reverseStr(test, 0, len(test) - 1)
    print(result)
