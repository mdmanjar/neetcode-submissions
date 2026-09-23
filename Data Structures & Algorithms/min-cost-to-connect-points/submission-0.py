class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n=len(points)

        def mahn(point1,point2):
            return abs(point1[0]-point2[0])+abs(point1[1]-point2[1])

        data=sorted((mahn(points[i],points[j]),i,j) for i in range(n) for j in range(i+1,n))

        p=[-1]*n

        def find(a):
            if p[a]<0:return a
            p[a]=find(p[a])
            return p[a]

        def union(a,b):
            a,b=find(a),find(b)
            if a==b:return False
            if p[a]>p[b]:a,b=b,a
            p[a]+=p[b]
            p[b]=a
            return True

        cost=0

        for w,i,j in data:
            if union(i,j):
                cost+=w

        return cost


        