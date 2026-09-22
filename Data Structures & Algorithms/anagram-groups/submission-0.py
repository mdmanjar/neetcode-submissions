class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp=defaultdict(list)

        for word in strs:
            mp[''.join(sorted(word))].append(word)
        
        return [v for v in mp.values()]
        