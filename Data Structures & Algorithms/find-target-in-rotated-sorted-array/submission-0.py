class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def mid():
            left,right=0,len(nums)-1

            while left<right:
                mid=left+(right-left)//2

                if nums[mid]>nums[right]:
                    left=mid+1
                else:
                    right=mid
            return left

        def bs(left,right):


            while left<=right:
                mid=left+(right-left)//2

                if nums[mid]==target:
                    return mid
                elif target>nums[mid]:
                    left=mid+1
                else:
                    right=mid-1

            return -1
        mn=mid()
        x=bs(0,mn-1)
        if x!=-1:return x
        return bs(mn,len(nums)-1)