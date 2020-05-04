from pystack import Stack
class DatabaseException(Exception):
    def __init__(self,err='parentheses not match!'):
        Exception.__init__(self,err)
str_code = input()
stack = Stack()
try:
    for item in str_code:
        if item == '(' :stack. push(1)
        elif item == ')':
            if stack.isEmpty() : raise DatabaseException
            else: stack.pop()
        else: pass
    if stack.size() == 0: print("parentheses match!")
    else: raise DatabaseException
except DatabaseException as error : print(error)
