class Stack:
    def __init__(self):
        self.stack = []
    def push(self,item):
        self.stack.append(item)
    def pop(self):
        top = self.stack[-1]
        del self.stack[-1]
        return top
    def peek(self):
        return self.stack[-1]
    def isEmpty(self):
        if len(self.stack) == 0: return True
        else: return False
    def size(self):
        return len(self.stack)
