class Solution:
    def isNStraightHand(self, hand: List[int], k: int) -> bool:
        if len(hand)%k!=0:
            return False
        mp = defaultdict(int)

        for e in hand:
            mp[e]+=1
        
        def check(u):
            sz=0
            while sz<k and mp[u]:
                sz+=1
                mp[u]-=1
                u+=1

            return sz==k

        hand.sort()
        
        for e in hand:
            if mp[e]:
                if not check(e):
                    return False
        return True

        





        
        
        