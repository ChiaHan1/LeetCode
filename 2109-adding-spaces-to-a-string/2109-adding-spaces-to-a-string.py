class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        result = [None] * (len(s) + len(spaces))
        
        # two pointers for the result and spaces
        result_idx = 0
        space_idx = 0
        
        for c in range(len(s)):
            if space_idx < len(spaces) and c == spaces[space_idx]:
                # append a space to the result
                result[result_idx] = ' '
                # advance the pointers
                result_idx += 1
                space_idx += 1
            # append the current character to the result
            result[result_idx] = s[c]
            result_idx += 1
            
        return ''.join(result)