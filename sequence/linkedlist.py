#!/usr/bin/env python
# -*- coding:utf-8 -*-
from __future__ import division
from __future__ import unicode_literals
from __future__ import print_function


class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
        self.size = 0


class LinkedList(object):
    def __init__(self):
        self.head = None

    def __len__(self):
        return self.size

    def insert(self, data):
        self.head = Node(data, self.head)
        self.size += 1

    def append(self, data):
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = Node(data)
        self.size += 1
