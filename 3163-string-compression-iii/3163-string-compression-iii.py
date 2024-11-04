class Solution:
    def compressedString(self, word: str) -> str:
        comp = []
        # pointer to current character
        i = 0
                
        while (i < len(word)):
            # current character
            current = word[i]
            # count of consecutive current character
            count = 1
            i += 1
            
            while (i < len(word) and current == word[i]):
                i += 1
                count += 1
                # if count is 9
                if count == 9:
                    # add to the result
                    comp.append(str(count) + current)
                    # reset the count
                    count = 0
                    
            # end of consecutive
            if count != 0:
                comp.append(str(count) + current)
        
        # make the list of result a single string
        return "".join(comp)
            