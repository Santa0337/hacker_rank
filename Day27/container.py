class Solution:
    def maxArea(self, height: List[int]) -> int:
        s = 0 
        e = len(height) - 1 
        max_area = 0 
        while s < e:
            area = (e - s) * min(height[s], height[e]) 
            max_area = max(max_area, area) 
            if height[s] < height[e]: 
                s += 1 
            else: 
                e -= 1 
        return max_area



        
