class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n=len(accounts)
        p=[-1]*n

        def find(a):
            if p[a]<0:return a
            p[a]=find(p[a])
            return p[a]

        def union(a,b):
            a,b=find(a),find(b)
            if a==b:return
            if p[a]>p[b]:a,b=b,a
            p[a]+=p[b]
            p[b]=a

        def index(a):
            return abs(p[find(a)])-1

        mp={}

        for i,account in enumerate(accounts):
            for email in account[1:]:
                if email in mp:
                    union(i,mp[email])
                else:
                    mp[email]=i
        idx=-1
        ans=[]


        for i in range(n):
            if p[i]<0:
                p[i]=idx
                idx-=1
                ans.append([])
        for email,idx in mp.items():
            ans[index(idx)].append(email)
        for e in ans:
            e.sort()
        for i in range(n):
            if p[i]<0:
                ans[index(i)]=accounts[i][:1]+ans[index(i)]
        return ans