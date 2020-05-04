#from StackStudy.pystack import Stack
from pystack import Stack
num_B = Stack()
num_D,target = map(int,input().split(' '))
while num_D > 0:
    n = num_D % target
    if n < 10: num_B.push(n)
    else: num_B.push(chr(ord('A')+n-10))
    num_D = num_D // target
while not num_B.isEmpty(): print(num_B.pop(),end='')
print()
    