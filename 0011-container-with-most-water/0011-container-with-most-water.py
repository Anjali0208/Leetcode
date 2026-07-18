class Solution:
    def maxArea(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        m=0
        for i in range(len(height)-1):
            width = r-l
            h = min(height[l], height[r])
            area = width*h
            if area>m:
                m = area
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
            
        return m