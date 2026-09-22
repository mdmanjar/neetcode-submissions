
class Solution:
    def evalRPN(self, token: List[str]) -> int:
        def cal(a,b,op):
            if op=='+':return a+b
            elif op=='-':return a-b
            elif op=='*':return a*b
            return abs(a)//abs(b)*(-1 if (a<0)^(b<0) else 1)

        top=-1

        for i in range(len(token)):
            if token[i] in '+-*/':
                token[top-1]=str(cal(int(token[top-1]),int(token[top]),token[i]))
                top-=1
            else:
                top+=1
                token[top]=token[i]

        return int(token[0])
