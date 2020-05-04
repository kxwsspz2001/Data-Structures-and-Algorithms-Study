#from StackStudy.pystack import Stack
from pystack import Stack
def numb(): pass
def express():pass
def judge():pass
def bracket():pass
def prefix():pass
def postfix():pass

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
        if str_[i] in '0123456789': num.push(int(str_[i]))     #如果当前字符为数字，将数字堆入栈中
        elif str_[i] in '+-*/()':                                          #如果当前字符为符号
            if not num.isEmpty():
                expression.append(numb(num))                  #将栈中堆放的数放入表达式
                num = Stack()                                           #初始化栈
            expression.append(str_[i])                              #将符号放入表达式
    if str_[-1] != ')': expression.append(numb(num))       #如果最后一位是数字，将最后栈中堆放的数放入表达式
    del num                                                                #释放内存
    return expression

def judge(expression):
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

def prefix(infix=None,char_1='(',char_2=')'):
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

def postfix(infix=None):
    """后缀"""
    if infix == None: infix = bracket()    
    return prefix(infix[::-1],')','(')[::-1]





