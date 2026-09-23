class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1=='0' or num2=='0':return '0'
        num1=list(map(int,num1[::-1]))
        num2=list(map(int,num2[::-1]))
        m=len(num1)
        n=len(num2)
        ans=[]
        level=0

        for i in range(m):
            carry=0
            k=level
            for j in range(n):
                if k==len(ans):ans.append(0)
                mul=num1[i]*num2[j]+carry+ans[k]
                ans[k]=mul%10
                carry=mul//10
                k+=1
            if carry:
                if k==len(ans):ans.append(carry)
            level+=1

        return ''.join(map(str,ans[::-1]))