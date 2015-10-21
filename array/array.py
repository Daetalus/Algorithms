#!/usr/bin/env python
# -*- coding:utf-8 -*-
from __future__ import division
from __future__ import unicode_literals
from __future__ import print_function


def removeElement(A, elem):
    # too Simple, but confused me at first time
    cur = 0
    forward = 0
    while forward < len(A):
        if A[forward] != elem:
            A[cur] = A[forward]
            cur += 1
        forward += 1
    return cur
