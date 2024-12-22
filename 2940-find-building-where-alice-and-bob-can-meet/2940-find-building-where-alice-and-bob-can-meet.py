class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        ans = [-1] * len(queries)
        # store the new queries for each building
        new_quries = [[] for _ in range(len(heights))]
        # monotonic stack to keep the leftmost valid building
        mono_stack = []
        
        for i, (a, b) in enumerate(queries):
            if a > b:
                # swap them to make sure alice is on the left
                a, b = b, a
            if heights[b] > heights[a] or a == b:
                # if bob's building is tall directly
                ans[i] = b
            else:
                new_quries[b].append((heights[a], i))
        
        # process buildings from right to left
        for i in range(len(heights) - 1, -1, -1):
            # for each query at the current building i (every query where bob is at this building)
            for height_a, idx in new_quries[i]:
                # perform binary search to find the appropriate building
                left, right = 0, len(mono_stack) - 1
                # position of the leftmost valid building
                pos = -1
                while left <= right:
                    mid = (left + right) // 2
                    if mono_stack[mid][0] > height_a:
                        pos = mid
                        left = mid + 1
                    else:
                        right = mid - 1
                # if the position is not found
                if pos != -1:
                    ans[idx] = mono_stack[pos][1]
            # maintain the monotonic stack where the heights are increasing
            while mono_stack and mono_stack[-1][0] <= heights[i]:
                mono_stack.pop()
            # add the height of this building to the monotonic stack
            mono_stack.append((heights[i], i))
        
        return ans