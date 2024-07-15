from random import choice

class RandomizedSet:

    def __init__(self):
        # a dict of indices
        self.dict = {}
        # a list of values
        self.list = []

    def insert(self, val: int) -> bool:
        # if the value is already in the set
        if val in self.dict:
            return False
        # add the index of the new value
        self.dict[val] = len(self.list)
        self.list.append(val)
        return True

    def remove(self, val: int) -> bool:
        # if the value exists
        if val in self.dict:
            # the index of the value
            index = self.dict[val]
            # swap the element with the last element to achieve O(1)
            self.dict[self.list[-1]] = index
            self.list[-1], self.list[index] = self.list[index], self.list[-1]
            self.list.pop()
            del self.dict[val]
            return True
        return False

    def getRandom(self) -> int:
        return choice(self.list)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()