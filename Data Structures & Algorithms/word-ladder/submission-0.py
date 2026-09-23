import string
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:return 0

        q=deque([beginWord])
        level=1
        st={beginWord}
        wordList=set(wordList)

        while q:
            for _ in range(len(q)):
                cur=q.popleft()
                for i in range(len(cur)):
                    old_chr=cur[i]
                    word=list(cur)

                    for c in string.ascii_lowercase:
                        if old_chr==c:continue
                        word[i]=c
                        new_word=''.join(word)

                        if new_word in wordList and new_word not in st:
                            if new_word==endWord:
                                return level+1
                            st.add(new_word)
                            q.append(new_word)

                        word[i]=old_chr
            level+=1

        return 0