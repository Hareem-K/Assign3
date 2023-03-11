"""
Class: ENSF 338, W23
Names: Hareem Khan, Eeman Abid
Assignment: 3
"""

import sys

# Define a stack class

class Stack:
    def __init__(self):
        self.items = []
        
    def push(self, item):
        self.items.append(item)
        
    def pop(self):
        return self.items.pop()
    
    def is_empty(self):
        return self.items == []
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        
# Write a tokenizer function for arithmetic expression

def tokenize(expr):
    tokens = []
    token = ''
    for char in expr:
        if char in ['(', ')', ' ', '+', '-', '*', '/']:
            if token:
                tokens.append(token)
                token = ''
            if char != ' ':
                tokens.append(char)
        else:
            token += char
    if token:
        tokens.append(token)
    return tokens

def apply_operator(op, arg1, arg2):
    if op == '+':
        return arg1 + arg2
    elif op == '-':
        return arg1 - arg2
    elif op == '*':
        return arg1 * arg2
    elif op == '/':
        return arg1 / arg2

def evaluate(expr):
    if expr.isdigit():
        return int(expr)
    
    stack = Stack()
    tokens = tokenize(expr)
    operators = ['+', '-', '*', '/']

    for token in tokens:
        if token == '(':
            continue
        elif token in operators:
            stack.push(token)
        elif token[-1] == ')':
            arg2 = stack.pop()
            arg1 = stack.pop()
            op = stack.pop()
            result = apply_operator(op, arg1, arg2)
            stack.push(result)
            if len(stack.items) == 1:
                break
        else:
            stack.push(int(token))
    return stack.pop()

if __name__ == '__main__':
    expr = sys.argv[1]
    result = evaluate(expr)
    print(result)