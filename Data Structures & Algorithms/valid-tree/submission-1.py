class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        p=[-1]*n

        def find(a):
            if p[a]<0:return a
            p[a]=find(p[a])
            return p[a]
        def union(a,b):
            a=find(a)
            b=find(b)
            if a==b:return False

            if p[a]>p[b]:a,b=b,a
            p[a]+=p[b]
            p[b]=a
            return True
        
        for u,v in edges:
            if not union(u,v):return False
        count=0
        for i in range(n):
            if p[i]<0:count+=1

        return count==1
        