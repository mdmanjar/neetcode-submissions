class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        ans=0
        stack=[]
        n=len(heights)

        for i in range(n+1):

            t=0
            if i<n:
                t=heights[i]

            while stack and heights[stack[-1]]>t:
                height=heights[stack.pop()]
                width=i if not stack else i-stack[-1]-1
                ans=max(ans,height*width)

            stack.append(i)
        return ans