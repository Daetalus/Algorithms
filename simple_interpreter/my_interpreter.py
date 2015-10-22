#!/usr/bin/env python
# -*- coding:utf-8 -*-
from __future__ import division
from __future__ import unicode_literals
from __future__ import print_function

# This is a toy interpreter that used to demonstrate the concept of
# interpreter. Feel free to use it.


class IntObject(object):
    def __init__(self, value):
        self.value = value

    def add(self, other):
        return IntObject(self.value + other.value)

    def sub(self, other):
        return IntObject(self.value - other.value)

    def __str__(self):
        return str(self.value)


INT, OP_PLUS, OP_SUB = 'INT', 'OP_PLUS', 'OP_SUB'


class Token(object):
    def __init__(self, type, value):
        self.value = value
        self.type = type


class Interpreter(object):
    def __init__(self, expr):
        self.expr = expr
        self.tokens = []

    def parse(self):
        expr = self.expr
        units = expr.split()
        for unit in units:
            try:
                result = int(unit)
                token = Token(INT, result)
                self.tokens.append(token)
            except ValueError:
                pass
            if unit == '+':
                token = Token(OP_PLUS, unit)
                self.tokens.append(token)
            if unit == '-':
                token = Token(OP_SUB, unit)
                self.tokens.append(token)

    def eval(self):
        self.parse()
        left = self.tokens[0]
        right = self.tokens[2]
        lhs = IntObject(left.value)
        rhs = IntObject(right.value)

        op = self.tokens[1]
        if op.type == OP_PLUS:
            return lhs.add(rhs).value
        elif op.type == OP_SUB:
            return lhs.sub(rhs).value


def run_repl():
    while True:
        try:
            expr = raw_input("> ")
        except (EOFError, KeyboardInterrupt):
            break
        if not expr:
            continue
        repl = Interpreter(expr)
        result = repl.eval()
        print(result)

if __name__ == '__main__':
    run_repl()
