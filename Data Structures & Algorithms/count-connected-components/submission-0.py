class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        p=[-1]*n 

        def find(a):
            if p[a]<0:return a
            p[a]=find(p[a])
            return p[a]
        
        def union(a,b):
            a,b=find(a),find(b)
            if a!=b:p[b]=a
        
        for u,v in edges:union(u,v)
        return sum(1 for i in range(n) if p[i]<0)
        