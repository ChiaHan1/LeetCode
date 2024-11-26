class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        # a hash set that contains all the vertices
        candidates = set(range(n))
        
        # iterate through all the edges
        for _, l in edges:
            candidates.discard(l)
        
        return next(iter(candidates)) if len(candidates) == 1 else -1