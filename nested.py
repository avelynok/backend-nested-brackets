#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
checks whether expressions are properly nested. If the expression is not
properly nested program should determine the position of the offending bracket.
"""
__author__ = "Avelyno Koumaka"

import sys

open_list = ["(*", "(", "[", "{", "<"]
close_list = ["*)", ")", "]", "}", ">"]


def is_nested(line):
    """Validate a single input line for correct nesting"""
    stack = []
    count = 1

    def validate_open_list(token, stack):
        if not line:
            return token
        for paren in open_list:
            if line.startswith(paren):
                token = paren
                stack.append(token)
                break
        return token

    def validate_close_list(token):
        if not line:
            return token
        for paren in close_list:
            if line.startswith(paren):
                token = paren
                if not stack or open_list.index(stack.pop()) != \
                        close_list.index(paren):
                    return "NO"
                break
        return token
    while line:
        token = line[0]
        token = validate_open_list(token, stack)
        token = validate_close_list(token)
        if token == "NO":
            return "NO " + str(count)
        count += 1
        line = line[len(token):]

    if not stack:
        return "YES"
    else:
        return "NO " + str(count - 1)


def main(args):
    """Open the input file and call `is_nested()` for each line"""
    # Results: print to console and also write to output file
    with open('input.txt', 'r') as f:
        with open('result.txt', 'w') as result:
            for line in f:
                result.write(is_nested(line) + "\n")
                print(is_nested(line))


if __name__ == '__main__':
    main(sys.argv[1:])
