class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        if len(trust) < n - 1:
            return -1
        
        # using n + 1 because people are labeled from 1 to n
        in_minus_out_degree = [0] * (n + 1)
        
        # for each relationship
        for a, b in trust:
            # a's outdegree
            in_minus_out_degree[a] -= 1
            # b's indegree
            in_minus_out_degree[b] += 1
            
        for i in range(1, n + 1):
            if in_minus_out_degree[i] == n - 1:
                return i
            
        return -1