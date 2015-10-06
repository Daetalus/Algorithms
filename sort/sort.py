#!/usr/bin/env python
# -*- coding:utf-8 -*-
from __future__ import division
from __future__ import unicode_literals
from __future__ import print_function


aux = list()


# Classical merge sort
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


def mergeSort_recursive(arr, aux, low, high):
    if high <= low:
        return

    mid = low + (high - low) / 2
    mergeSort_recursive(arr, aux, low, mid)
    mergeSort_recursive(arr, aux, mid + 1, high)
    merge(arr, aux, low, mid, high)


# Stable
# Time: o(nlogN)
# Space: o(N)
def mergeSort(arr):
    n = len(arr)
    mid = n / 2
    mergeSort_recursive(arr, 0, mid)
    mergeSort_recursive(arr, mid + 1, n)
    return merge(arr, 0, mid, n)


# Pythonic merge sort
def mergePythonic(a, b):
    result = []
    i, j = (0, 0)
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
    if a[i:]:
        result.extend(a[i:])
    if b[j:]:
        result.extend(b[j:])
    return result


def mergesort(arr):
    n = len(arr)
    if n <= 1:
        return arr
    a1 = mergesort(arr[:n/2])
    a2 = mergesort(arr[n/2:])
    return mergePythonic(a1, a2)


# Unstable
# Time: o(N^2)
# Space: o(N^2)
def selectionSort(a):
    for i in range(len(a)):
        min = i
        for j in range(i, len(a)):
            if a[j] < a[min]:
                min = j
        a[i], a[min] = a[min], a[i]
    return a


# Stable
# Time: o(N^2), best: o(N)
# Space: o(1)
def bubbleSort(a):
    for i in range(len(a)):
        for j in range(i, len(a)):
            if a[i] > a[j]:
                a[i], a[j] = a[j], a[i]
    return a


# Stable
# Time: o(N^2), best: o(N)
# Space: o(1)
def insertionSort(a):
    if not a or len(a) == 1:
        return a

    for i in range(len(a)):
        item = a[i]
        j = i
        while j > 0 and a[j - 1] > item:
            a[j] = a[j - 1]
            j -= 1
        a[j] = item
    return a


# Unstable:
# Time: O(n^2)
def partition(a, low, high):
    start = low + 1
    end = high
    pivotItem = a[low]
    while True:
        while a[start] <= pivotItem:
            start += 1
            if (start >= high):
                break
        while a[end] > pivotItem:
            end -= 1
            if (end <= low):
                break
        if (start >= end):
            break
        a[start], a[end] = a[end], a[start]

    a[low], a[end] = a[end], a[low]
    return end


def _quickSort(a, low, high):
    if high <= low:
        return
    pivot = partition(a, low, high)
    _quickSort(a, low, pivot - 1)
    _quickSort(a, pivot + 1, high)
    return a


# Unstable
# Time: o(nlogn) on average, o(n^2) for the worst case
# Space: o(nlogn)
def quickSort(a):
    return _quickSort(a, 0, len(a) - 1)


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


def testQuickSort1():
    seq = [3, 5, 1, 3, 9, 4, 6, 3, 6, 7, 4, 3, 2, 5, 7, 8]
    sorted_seq = sorted(seq)
    assert(quickSortPythonic(seq) == sorted_seq)
    print('Pythonic quick sort tests passed!')
    assert(quickSort(seq) == sorted_seq)
    print('Classic quick sort tests passed!')
    assert(selectionSort(seq) == sorted_seq)
    print("Selection sort passed!")
    assert(insertionSort(seq) == sorted_seq)
    print('Insertion sort passed!')
    assert(bubbleSort(seq) == sorted_seq)
    print('Bubble sort passed!')

if __name__ == '__main__':
    testQuickSort1()
