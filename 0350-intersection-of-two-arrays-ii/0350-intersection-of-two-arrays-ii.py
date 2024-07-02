from collections import defaultdict

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count1 = defaultdict(int)
        count2 = defaultdict(int)
        
        intersection = []
        
        for n in nums1:
            count1[n] += 1
        
        for n in nums2:
            if count1[n] > count2[n]:
                intersection.append(n)
                count2[n] += 1
        return intersection
        