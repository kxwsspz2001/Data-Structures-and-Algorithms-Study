from pystack import Stack
class DatabaseException(Exception):
    def __init__(self,err='parentheses not match!'):
        Exception.__init__(self,err)


str_code = input()
stack = Stack()
try:
    for item in str_code:
        if item == '(' :stack.push(1)
        elif item == ')':
            if stack.isEmpty() or stack.peek() != 1: raise DatabaseException
            else: stack.pop()
        elif item == '[' :stack.push(2)
        elif item == ']':
            if stack.isEmpty() or stack.peek() != 2: raise DatabaseException
            else: stack.pop()
        elif item == '{' :stack.push(3)
        elif item == '}':
            if stack.isEmpty() or stack.peek() != 3: raise DatabaseException
            else: stack.pop()
    if stack.size() == 0: print("parentheses match!")
    else: raise DatabaseException
except DatabaseException as error : print(error)
