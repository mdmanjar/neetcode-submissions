class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        mp=[[None]*26 for _ in range(26)]

        def add(word):
            i,j=index(word)
            mp[i][j]=(word,mp[i][j])
        
        def index(word):
            return ord(word[0])-97,ord(word[-1])-97
        ans=0

        for word in words[::-1]:
            i,j=index(word)
            node=mp[i][j]

            while node:
                if node[0].startswith(word) and node[0].endswith(word):ans+=1
                node=node[1]
            add(word)
        return ans

        