class Solution:
    def reverseParentheses(self, s: str) -> str:
        n = len(s)
        # indices of open parentheses
        start_index = []
        
        pair = [0] * n
        
        # pair up parentheses
        for i in range(n):
            if s[i] == '(':
                start_index.append(i)
            if s[i] == ')':
                j = start_index.pop()
                # record the index of the other side
                pair[i] = j
                pair[j] = i
        
        # build the result
        result = []
        # current index of the string
        current = 0
        # initially start from positive direction
        direction = 1
        
        while current < n:
            # if current character is a parenthesis
            if s[current] == '(' or s[current] == ')':
                # go to the other side of the parentheses pair
                current = pair[current]
                # change the direction of current index moving towards
                direction = -direction
            else:
                result.append(s[current])
            
            current += direction
        
        return "".join(result)
                