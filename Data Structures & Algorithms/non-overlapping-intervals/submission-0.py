class Solution:
    def eraseOverlapIntervals(self, arr: List[List[int]]) -> int:
        arr.sort(key=lambda x:x[0])

        prev=0
        ans=0

        for i in range(1,len(arr)):
            if arr[prev][1]>arr[i][0]:
                ans+=1
                if arr[i][1]<arr[prev][1]:
                    prev=i
            else:
                prev=i

        return ans
        

        