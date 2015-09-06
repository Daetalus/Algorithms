#!/usr/bin/env python
# -*- coding:utf-8 -*-
from __future__ import division
from __future__ import unicode_literals
from __future__ import print_function


class Node(object):
    def __init__(self, data, next):
        self.data = data
        self.next = next


class LinkedList(object):
    def __init__(self):
        self.head = None
