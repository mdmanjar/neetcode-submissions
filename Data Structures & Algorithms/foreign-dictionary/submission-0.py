class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        g=[[] for _ in range(26)]
        deg=[0]*26
        chars=set(''.join(words))

        for i in range(len(words)-1):
            a,b=words[i],words[i+1]
            found=False

            for x,y in zip(a,b):
                if x!=y:
                    u,v=ord(x)-97,ord(y)-97
                    g[u].append(v)
                    deg[v]+=1
                    found=True
                    break

            if not found and len(a)>len(b):
                return ""

        q=deque(i for i in range(26) if deg[i]==0 and chr(i+97) in chars)
        ans=[]

        while q:
            u=q.popleft()
            ans.append(chr(u+97))

            for v in g[u]:
                deg[v]-=1
                if deg[v]==0:
                    q.append(v)

        return ''.join(ans) if len(ans)==len(chars) else ""