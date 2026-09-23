class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n=len(edges)
        p=[-1]*(n+1)

        def find(a):
            if p[a]<0:return a
            p[a]=find(p[a])
            return p[a]
        
        def union(a,b):
            a=find(a)
            b=find(b)
            if a==b:return True
            p[a]=b
            return False
        
        for u,v in edges:
            if union(u,v):return [u,v]
        