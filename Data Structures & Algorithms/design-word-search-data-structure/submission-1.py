class WordDictionary:

    def __init__(self):
        self.root={}
        

    def addWord(self, word: str) -> None:
        t=self.root

        for c in word:t=t.setdefault(c,{})
        t['#']=True
        

    def search(self, word: str) -> bool:

        def dfs(root,i):
            if i==len(word):return '#' in root
            if word[i] in root:
                return dfs(root[word[i]],i+1)
            if word[i]!='.':
                return False
            for k,v in root.items():
                if k!='#' and dfs(v,i+1):
                    return True
            return False
        return dfs(self.root,0)
        
