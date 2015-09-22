#!/usr/bin/env python
# -*- coding:utf-8 -*-
from __future__ import division
from __future__ import unicode_literals
from __future__ import print_function


aux = list()

def merge(list_a, low, mid, high):
    i = low,
    j = mid + 1

    for k in range(low, high):
        aux[k] = list_a[k]

    for k in range(low, high):
        if i > mid:
            list_a[k] = aux[j]
            j += 1
        elif j > high:
            list_a[k] = list_a[i]
            i += 1
        elif aux[i] < aux[j]:
            list_a[k] = list_a[i]
            i += 1
        else:
            list_a[k] = list_a[j]
            j += 1


def mergeSort(arr):
    pass


def selectSort(a):
    for i in range(len(a)):
        min = i
        for j in range(i, len(a)):
            if a[j] < a[min]:
                min = j
        a[i], a[min] = a[min], a[i]
    return a


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


# This method need create local variable in each call.
# The original method doesn't need to create local variable.
# The space complexity seems is O(NlogN) TODO, need verify it
# tradictional quickSort space complexity is O(logN)
# and time complexity is O(logN)
# This is three way quick sort. Time complexity between O(N) and O(logN)
# We can use a help function(with index parameter) to reduce the space
# complexity
def quickSortPythonic(a):
    less = []
    equal = []
    greater = []

    if len(a) > 1:
        pivot = a[0]
        for item in a:
            if item < pivot:
                less.append(item)
            elif item > pivot:
                greater.append(item)
            else:
                equal.append(item)
        return quickSortPythonic(less) + equal + quickSortPythonic(greater)
    else:
        return a
