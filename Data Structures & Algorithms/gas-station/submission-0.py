class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        if sum(gas)<sum(cost):
            return -1
        
        ans=0
        bal=0

        for i in range(len(gas)):
            bal=(bal+gas[i])-cost[i]

            if bal<0:
                bal=0
                ans=i+1

        return ans