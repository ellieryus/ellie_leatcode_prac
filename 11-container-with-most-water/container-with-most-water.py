class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l = 0
        r = len(height)-1 # index
        maximum = 0
        while l < r:
            h = min(height[r], height[l]) 
            maximum = max(maximum, h*(r-l))
            if height[l] < height[r]:
                l+=1
            else:
                r-=1
        return maximum
        