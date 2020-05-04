class Stack:
    def __init__(self,stack = []):
        self.stack_ = list(stack)[::-1]
    def push(self,item):
        self.stack_.append(item)
    def pop(self):
        top = self.stack_[-1]
        del self.stack_[-1]
        return top
    def peek(self):
        if not self.isEmpty(): return self.stack_[-1]
    def isEmpty(self):
        if len(self.stack_) == 0: return True
        else: return False
    def size(self):
        return len(self.stack_)


