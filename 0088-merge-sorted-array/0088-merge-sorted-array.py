class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        # the actual list 1
        n1 = nums1[:m]
        
        if m == 0:
            for i in range(len(nums2)):
                nums1[i] = nums2[i]
            return
        if n == 0:
            return
        
        # pointers
        p1 = 0
        p2 = 0
        
        for i in range(n + m):
            if n1[p1] <= nums2[p2]:
                nums1[i] = n1[p1]
                p1 += 1
            else:
                nums1[i] = nums2[p2]
                p2 += 1
                
            if p1 == m:
                nums1[i+1:] = nums2[p2:]
                break
            if p2 == n:
                nums1[i+1:] = n1[p1:]
                break
        