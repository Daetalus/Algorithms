#!/usr/bin/env python
# -*- coding:utf-8 -*-
from __future__ import division
from __future__ import unicode_literals
from __future__ import print_function


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def removeElements(head, val):
    dummy = ListNode(0)
    dummy.next = head
    cur = head
    last = dummy
    while cur:
        if cur.val == val:
            last.next = cur.next
        else:
            last = cur
        cur = cur.next
    return dummy.next


# Very important
def swapPairs(head):
    dummy = ListNode(0)
    dummy.next = head
    cur = dummy

    while cur.next and cur.next.next:
        next = cur.next.next.next
        first = cur.next
        second = cur.next.next
        cur.next = second
        cur.next.next = first
        cur = cur.next.next
        cur.next = next

    return dummy.next


def deleteDuplicates(head):
    if not head or not head.next:
        return head

    cur = head
    next = cur.next
    # use next as sentinel!!!
    while next:
        if next.val == cur.val:
            cur.next = cur.next.next
        else:
            cur = next
        next = cur.next
    return head


def nthToLast(head):
    # recursive?
    pass
