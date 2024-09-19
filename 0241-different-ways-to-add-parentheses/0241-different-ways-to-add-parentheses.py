class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        result = []
        for i in range(len(expression)):
            current = expression[i]
            # if current is an operator
            if current == '+' or current == '-' or current == '*':
                # recursively calculate all the possible results on the left
                left = self.diffWaysToCompute(expression[:i])
                # recursively calculate all the possible results on the right
                right = self.diffWaysToCompute(expression[i+1:])
                
                # calculate the result of all the possible combinations
                for l in left:
                    for r in right:
                        if current == '+':
                            result.append(l + r)
                        if current == '-':
                            result.append(l - r)
                        if current == '*':
                            result.append(l * r)
        # if result is empty (i.e. the expression only has one number without operators)
        if result == []:
            result.append(int(expression))

        return result
                