class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        n=len(nums)
        cmp=n
        if n==1:return True
        if 1 in nums:return False

        p=[-1]*n

        def find(a):
            if p[a]<0:return a
            p[a]=find(p[a])
            return p[a]

        def union(a,b):
            nonlocal cmp
            a,b=find(a),find(b)
            if a==b:return
            if p[a]>p[b]:a,b=b,a
            p[a]+=p[b]
            p[b]=a
            cmp-=1

        mp={}

        def fact(num,j):
            i=2

            while i*i<=num:
                if num%i==0:
                    if i in mp:union(mp[i],j)
                    mp[i]=j
                    while num%i==0:
                        num//=i
                i+=1

            if num>1:
                if num in mp:union(mp[num],j)
                else:mp[num]=j

        for i,e in enumerate(nums):
            fact(e,i)

        return cmp==1