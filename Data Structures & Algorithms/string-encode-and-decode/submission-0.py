class Solution:

    def encode(self, strs: List[str]) -> str:
        ans=''
        for word in strs:
            ans+=str(len(word))+'#'+word
        return ans

    def decode(self, s: str) -> List[str]:
        ans=[]
        i=0

        while i<len(s):
            j=i
            while s[j]!='#':
                j+=1

            n=int(s[i:j])
            ans.append(s[j+1:j+1+n])
            i=j+1+n

        return ans