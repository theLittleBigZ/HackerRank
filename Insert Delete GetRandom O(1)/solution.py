import random

class RandomizedSet:

    def __init__(self):
        self.list = []

    def insert(self, val: int) -> bool:
        if self.list.count(val) == 0:
            self.list.append(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        if not self.list.count(val) == 0:
            self.list.remove(val)
            return True
        return False

    def getRandom(self) -> int:
        return self.list[random.randint(0, len(self.list)-1)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
