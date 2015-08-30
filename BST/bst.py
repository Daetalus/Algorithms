#!/usr/bin/env python
# -*- coding:utf-8 -*-
from __future__ import division
from __future__ import unicode_literals
from __future__ import print_function


class Node(object):
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


# recursive
def preOrderRecur(root):
    if not root:
        return
    print(root.value)
    if root.right:
        preOrderRecur(root.right)
    if root.left:
        preOrderRecur(root.left)


def postOrderRecur(root):
    if not root:
        return
    if root.right:
        postOrderRecur(root.right)
    if root.left:
        postOrderRecur(root.left)
    print(root.value)


# iterative
def preOrder(root):
    if root is None:
        return []

    stack = [root]
    preorder = []
    while stack:
        node = stack.pop()
        preorder.append(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return preorder
