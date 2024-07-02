class Solution:
    def maxArea(self, height: List[int]) -> int:
        # two pointers initially pointing at two ends
        left = 0
        right = len(height) - 1
        
        # maximum area contained
        max_area = 0
        
        while left < right:
            max_area = max(max_area, (right - left) * min(height[left], height[right]))
            
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
        return max_area