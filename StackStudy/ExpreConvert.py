#from StackStudy.pystack import Stack
from pystack import Stack
def numb(): pass
def express():pass
def judge():pass
def bracket():pass
def prefix_normal():pass
def postfix_normal():pass
def prefix_stack():pass
def postfix_stack():pass
def prefix_calculate():pass
def postfix_calculate():pass

def numb(stack):
    """
    数字处理
    从符号后一位开始将单个数字放入栈中至符号结束
    数字按位数取出
    """
    place = 1
    num = 0
    while not stack.isEmpty():
        num += stack.pop() * place
        place *= 10
    del stack
    return num

def express(str_=None):
    """处理表达式"""
    if str_ == None: str_ = input()
    num = Stack()
    expression = []
    for i in range(len(str_)):
        if str_[i] in '0123456789': num.push(int(str_[i]))     #检测当前字符为数字，将数字堆入栈中
        elif str_[i] in '+-*/()':                                          #检测当前字符为符号
            if not num.isEmpty():
                expression.append(numb(num))                  #将栈中堆放的数放入表达式
                num = Stack()                                           #初始化栈
            expression.append(str_[i])                              #将符号放入表达式
    if str_[-1] != ')': expression.append(numb(num))       #检测最后一位是数字，将最后栈中堆放的数放入表达式
    del num                                                                #释放内存
    return expression

def judge(expression):
    """去除多余括号"""
    #i = 0
    #for item in expression:                 #计算运算符数量
    #    if str(item) in '+-*/': i+=1
    #j=i+1
    #while i<j:
    #    j=0
    #    for item in expression:             #计算括号数量
    #        if item == '(': j+=1
    #    if i >= j :break
    #    place = Stack()                        #位置
    #    couple = Stack()                      #双括号
    #    single = Stack()                       #单括号
    #    k = 0
    #    while k < (len(expression)-1):
    #        if expression[k] == '(':
    #            if expression[k-1] != '(': single.push(1)   #检测是否单左括号 堆入单括号栈中
    #            elif expression[k-1] == '(' :
    #                couple.push(1)                                 #堆入双括号栈中
    #                place.push(k)                                   #堆入位置栈中
    #            k+=1
    #        elif expression[k] == ')':
    #            if expression[k+1] != ')' or not single.isEmpty():                        #检测是否为单右括号
    #                if not single.isEmpty(): single.pop()    #匹配单括号
    #                else:
    #                    couple.pop()                                #拆分双括号匹配单括号
    #                    if expression[place.peek()-2] != '(': single.push(1)
    #                    place.pop()
    #                k+=1
    #            else:
    #                del expression[k]                              #删除多余括号
    #                del expression[place.peek()]
    #                couple.pop()
    #                place.pop()
    #        else: k+=1
    #    del place                                                     #释放空间
    #    del couple
    #    del single          
    #return expression
    pass

def bracket(expression = None): 
    """全括号转换"""
    if expression == None: expression = express()
    def pare(str_):
        i=0
        while i < len(expression):
            if str(expression[i]) in str_ and expression[i-2] != '(':    #检测到运算符并且不在最小括号内
                if expression[i+1] != '(':expression.insert(i+2,')')       #检测运算符后是否为左括号
                else:
                    barckets = Stack()                                  
                    for j in range(i+1,len(expression)):                      #从运算符后左括号开始检测
                        if expression[j] == '(': barckets.push(0)           #检测左括号堆入栈中
                        elif expression[j] == ')':                                 #检测右括号
                            barckets.pop()                                          #从栈中匹配左括号
                            if barckets.isEmpty():                                #检测匹配完毕
                                expression.insert(j,')')                            #插入右括号
                                del barckets                                         #释放空间
                                break
                            
                
                if expression[i-1] != ')': expression.insert(i-1,'(')       #检测运算符前是否为右括号               
                else:
                    barckets = Stack()
                    for j in range(i)[::-1]:                                         #从运算符前右括号开始检测
                        if expression[j] == ')': barckets.push(0)           #检测右括号堆入栈中
                        elif expression[j] == '(':                                  #检测左括号
                            barckets.pop()                                          #从栈中匹配左括号
                            if barckets.isEmpty():                                #检测匹配完毕
                                expression.insert(j,'(')                            #插入左括号
                                del barckets                                         #释放空间
                                break
                i+=1
            i+=1
           
    pare('*/')
    pare('+-')
    return expression

def prefix_normal(infix=None,char_1='(',char_2=')'):
    """前缀"""
    if infix == None: infix = bracket()
    #for item in infix:
    #    print(item,end = '')
    #print()
    i = 0
    while i < len(infix):
        if str(infix[i]) in '+-*/':
            for j in range(i)[::-1]:
                if infix[j] == char_1:  #从第i个开始向前寻找括号 
                    infix[j] = infix[i]    #将左括号改为运算符
                    del infix[i]           #删除中缀运算符
                    break                 #结束循环
        else: i+=1
    i = 0
    while i < len(infix):
        if infix[i] == char_1: del infix[i]   #删除多余括号
        elif infix[i] == char_2: del infix[i]  
        else: i+=1
    return infix

def postfix_normal(infix=None):
    """后缀"""
    if infix == None: infix = bracket()    
    return prefix_normal(infix[::-1],')','(')[::-1]

def prefix_stack(infix=None):
    """前缀的堆栈算法"""
    if infix == None: infix = express()
    priority ={'+':1,'-':1,'*':2,'/':2,')':3}                       #设置优先级
    expression = []
    opstack = Stack()
    for item in infix[::-1]:                                         #倒序遍历
        if str(item) in '+-*/)':                                     #检测为字符
            if item == ')': opstack.push(item)                #排除右括号
            else:
                if opstack.isEmpty(): opstack.push(item)          #检测栈是否为空
                else:
                    if priority[opstack.peek()] > priority[item]:      #检测优先级
                        expression.append(opstack.pop())             #将优先级高的取出
                        opstack.push(item)                                 #优先级低的堆入栈中
                    else: opstack.push(item)                              #堆入栈中
        elif item == '(':                                                        #检测左括号，匹配右括号
            while not opstack.isEmpty():
                if not opstack.peek() in "()": expression.append(opstack.pop())     #将算术运算符放入表达式
                else: opstack.pop()                                          #删除括号
        else: expression.append(item)                                   #数字添加到表达式
    while not opstack.isEmpty():                                         #将栈中堆积的运算符放入表达式
        expression.append(opstack.pop())
    del opstack
    for item in expression:                                                  #删除多余括号
        if item == ')': expression.remove(item)
    return expression[::-1]

def postfix_stack(infix=None):
    """后缀的堆栈算法"""
    priority ={'+':1,'-':1,'*':2,'/':2}                                          #设置优先级
    if infix == None: infix = express()
    expression = []
    opstack = Stack()
    for item in infix:
        if str(item) in '+-*/':                                                  #检测运算符
            if opstack.peek() == '(': pass                                  #检测栈顶为左括号 直接将运算符堆入栈中
            else:
                if not opstack.isEmpty():                                    #检测栈是否为空
                    if priority[opstack.peek()] > priority[item]:        #与栈中运算符比较优先级
                        expression.append(opstack.pop())               #取出旧运算符           
            opstack.push(item)                                                #堆入新运算符
        elif item == '(': opstack.push(item)                              #将左括号堆入栈中
        elif item == ')':                                                          #检测右括号
            while opstack.peek() != "(": expression.append(opstack.pop())       #将括号内符号加入表达式       
        else: expression.append(item)                                     #将数字加入表达式
    while not opstack.isEmpty():                                            #将栈中剩余运算符加入表达式
        item = opstack.pop()
        if not item in"()": expression.append(item)
    del opstack
    return expression

def prefix_calculate(expression=None):
    if expression == None: expression = prefix_stack()
    num = Stack()
    i = 0
    while i < len(expression):
        item = expression[i]
        if str(item) in '+-*/': num.push(item)                  #运算符堆入栈中
        else:
            if  num.isEmpty(): num.push(item)                  #处理第一个数字
            else:
                if type(num.peek()) is str: num.push(item)   #检测栈顶是否为字符
                else:
                    num_1 = num.pop()                              #取出数字
                    operator = num.pop()                            #取出运算符
                    if operator == '+': expression.insert(i+1,num_1 + item)             #运算并将数字插入待处理
                    elif operator == '-': expression.insert(i+1,num_1 - item)
                    elif operator == '*': expression.insert(i+1,num_1 * item)
                    elif operator == '/': expression.insert(i+1,num_1 // item)
        i+=1
    return num.pop()

def postfix_calculate(expression=None):
    if expression == None: expression = postfix_stack()
    num = Stack()
    for item in expression:
        if type(item) is int: num.push(item)                        #将数字堆入栈中
        else:
            num_2 = num.pop()                                           #取出数字运算
            num_1 = num.pop()
            if item == '+': num.push(num_1 + num_2)
            elif item == '-': num.push(num_1 - num_2)
            elif item == '*': num.push(num_1 * num_2)
            elif item == '/': num.push(num_1 // num_2)
    return num.pop()



print(postfix_calculate())