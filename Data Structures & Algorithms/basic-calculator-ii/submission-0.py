
class Solution:
    def calculate(self, s: str) -> int:
        def cal(a,b,op):

            match(op):
                case '+':return a+b
                case '/':return a//b
                case '-':return a-b
                case '*':return a*b

        stack=[]
        num=0

        for c in s:
            if c==' ':continue
            if c.isdigit():
                num=num*10+(ord(c)-48)
            else:
                stack.append(num)
                stack.append(c)
                num=0
        stack.append(num)
        top=-1
        i=0
        while i<len(stack):
            if stack[i] in ('/','*'):
                stack[top]=cal(stack[top],stack[i+1],stack[i])
                i+=2

            else:
                top+=1
                stack[top]=stack[i]
                i+=1

        for i in range(2,top+1,2):
            stack[0]=cal(stack[0],stack[i],stack[i-1])
        return stack[0]