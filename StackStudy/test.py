#from StackStudy.pystack import Stack
from pystack import Stack
expression = list('(((1+2)*3)-((4-5))*(6+7))')
i,j=0,0
for item in expression:
    if str(item) in'+-*/': i+=1
    elif item == '(': j+=1
if i==j:
    place = Stack()
    couple = Stack()
    single = Stack()
    k = 0
    while k < (len(expression)-1):
        if expression[k] == '(':
            if expression[k-1] != '(' and k !=0 : single.push(1)
            elif expression[k-1] == '(' :
                couple.push(1)
                place.push(k)
            k+=1
        elif expression[k] == ')':
            if expression[k+1] != ')':
                if not single.isEmpty() : single.pop()
                else:
                    couple.pop()
                    place.pop()
                k+=1
            else:
                del expression[k]
                del expression[place.peek()]
                couple.pop()
                place.pop()
        else: k+=1
for item in expression:
    print(item,end='')
