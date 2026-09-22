class PrefixTree:

    def __init__(self):
        self.root={}
        

    def insert(self, word: str) -> None:
        t=self.root

        for c in word:
            t=t.setdefault(c,{})
        t['#']=True

    def search(self, word: str) -> bool:
        t=self.root
        for c in word:
            if c not in t:return False
            t=t[c]
        return '#' in t

    def startsWith(self, prefix: str) -> bool:
        t=self.root
        for c in prefix:
            if c not in t:return False
            t=t[c]
        return True
        
        