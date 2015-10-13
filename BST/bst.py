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


# recursive
def preOrderRecur(root):
    if not root:
        return
    print(root.value)

    if root.left:
        preOrderRecur(root.left)
    if root.right:
        postOrderRecur(root.right)


def postOrderInterative(root):
    if not root:
        return

    visited = set()
    stack = []
    result = []
    cur = root

    while cur or stack:
        if cur:
            stack.append(cur)
            # all the way to the left
            cur = cur.left
        else:
            cur = stack.pop()

            # right is existed and not visited, add current node
            # to stack
            if cur.right and cur.right not in visited:
                stack.append(cur)
                cur = cur.right
            # right visited or right is None
            # process current node
            else:
                # mark current node as visited
                visited.add(cur)
                result.append(cur.val)
                # mark current node as None
                # prevent jump to the left again
                cur = None


def postOrderRecur(root):
    if not root:
        return

    if root.left:
        postOrderRecur(root.left)
    if root.right:
        postOrderRecur(root.right)
    print(root.value)


def inOrderIterative(root):
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


def inOrderRecur(root):
    if not root:
        return

    if root.left:
        inOrderRecur(root.left)

    print(root.value)

    if root.right:
        inOrderRecur(root.right)


def levelOrder(root):
    if not root:
        return

    queue = []
    levelorder = []
    queue.append(root)
    while queue:
        cur = queue.pop(0)
        levelorder.append(cur)
        # do something to cur

        if cur.left:
            queue.append(cur.left)

        if cur.right:
            queue.append(cur.right)

    return levelorder
