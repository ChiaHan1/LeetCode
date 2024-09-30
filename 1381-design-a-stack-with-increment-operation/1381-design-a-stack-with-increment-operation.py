class CustomStack:

    def __init__(self, maxSize: int):
        # use array as the stack that stores [initial value, increment]
        self.stack = []
        # max size of the array
        self.max_size = maxSize

    def push(self, x: int) -> None:
        # if the stack is not full
        if len(self.stack) < self.max_size:
            # append to the stack
            self.stack.append([x, 0])

    def pop(self) -> int:
        # if the stack is empty
        if len(self.stack) == 0:
            return -1
        # pop from the stack
        val, inc = self.stack.pop()
        # if the stack is not empty and increment of last number is not 0
        if len(self.stack) > 0 and inc != 0:
            # the rest of the numbers also need to be incremented by inc
            self.stack[-1][1] += inc
        
        return val + inc

    def increment(self, k: int, val: int) -> None:
        # the index is in the middle
        if len(self.stack) >= k:
            # increment that number
            self.stack[k - 1][1] += val
        # k > the length of the stack
        elif len(self.stack) > 0:
            # increment the entire stack
            self.stack[-1][1] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)