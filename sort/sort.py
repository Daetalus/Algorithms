#!/usr/bin/env python
# -*- coding:utf-8 -*-
from __future__ import division
from __future__ import unicode_literals
from __future__ import print_function


def merge(list_a, list_b):
    pass


def mergeSort(arr):
    pass


def selectSort(arr):
    pass


def insertionSort(arr):
    pass


def partition(a, low, high):
    start = low + 1
    end = high
    pivotItem = a[low]
    while True:
        while a[start] < pivotItem:
            start += 1
            if (start == high):
                break
        while a[end] > pivotItem:
            end -= 1
            if (end <= low):
                break
        if (start >= end):
            break
        a[start] = a[end]

    a[low] = a[end]
    return end


def _quickSort(a, low, high):
    if high <= low:
        return
    pivot = partition(a, low, high)
    _quickSort(a, low, pivot - 1)
    _quickSort(a, pivot + 1, high)


def quickSort(a):
    _quickSort(a, 0, len(a) - 1)
