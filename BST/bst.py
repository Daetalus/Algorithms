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

    if root.left:
        preOrderRecur(root.left)
    if root.right:
        postOrderRecur(root.right)


def inOrderRecur(root):
    if not root:
        return

    if root.left:
        inOrderRecur(root.left)

    print(root.value)

    if root.right:
        inOrderRecur(root.right)


def postOrderRecur(root):
    if not root:
        return

    if root.left:
        postOrderRecur(root.left)
    if root.right:
        postOrderRecur(root.right)
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

def inOrder(root):
    if not root:
        return

    stack = []
    inorder = []
    cur = root
    while stack or cur:
        if cur:
            stack.append(cur)
            cur = cur.left
        else:
            cur = stack.pop()
            inorder.append(cur.value)
            cur = cur.right

    return inorder

def postOrder(root):
    if not root:
        return

    stack = []
    postorder = []
    cur = root
    while stack or cur:
        while cur:
            stack.append(cur)
            cur = cur.left

        if stack:
            cur = stack.pop()
            postorder.append(cur.value)
            cur = cur.right

    return postorder

def levelOrder(root):
    if not root:
        return

    queue = []
    queue.append(root)
    while queue:
        cur = queue.pop(0)
        # do something to cur

        if cur.left:
            queue.append(cur.left)

        if cur.right:
            queue.append(cur.right)
