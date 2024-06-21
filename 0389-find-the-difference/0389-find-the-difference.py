class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # s = list(s)
        # t = list(t)
        # 
        # for c in t:
        #     if c not in s:
        #         return c
        #     s.remove(c)

        extra = 0
        for c in s:
            extra ^= ord(c)
        for c in t:
            extra ^= ord(c)
        return chr(extra)