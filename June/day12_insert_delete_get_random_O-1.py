"""
Design a data structure that supports all following operations in average O(1) time.

insert(val): Inserts an item val to the set if not already present.
remove(val): Removes an item val from the set if present.
getRandom: Returns a random element from current set of elements. Each element must have the same probability of
being returned.
Example:
    // Init an empty set.
    RandomizedSet randomSet = new RandomizedSet();

    // Inserts 1 to the set. Returns true as 1 was inserted successfully.
    randomSet.insert(1);

    // Returns false as 2 does not exist in the set.
    randomSet.remove(2);

    // Inserts 2 to the set, returns true. Set now contains [1,2].
    randomSet.insert(2);

    // getRandom should return either 1 or 2 randomly.
    randomSet.getRandom();

    // Removes 1 from the set, returns true. Set now contains [2].
    randomSet.remove(1);

    // 2 was already in the set, so return false.
    randomSet.insert(2);

    // Since 2 is the only number in the set, getRandom always return 2.
    randomSet.getRandom();
"""

# getRandom will take longer than O(1) time implemented by turning a set into a tuple.
# A better, faster approach would be to not use a set, and instead just a list of values
# and a dictionary that stores the index of the values. Insert would easily be able to take
# O(1) time, get the index of the val then replace the val with the last val in the list,
# delete the val from the dict, and update the last vals postion in dict. Pop the last index
# of the list


import random

class RandomizedSet:

    def __init__(self):
        self.rset = set()

    def insert(self, val: int) -> bool:
        if val in self.rset:
            return False
        self.rset.add(val)
        print("added", val)
        return True

    def remove(self, val: int) -> bool:
        if val in self.rset:
            self.rset.remove(val)
            print("removed", val)
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(tuple(self.rset))



# For Testing
randomSet = RandomizedSet()
print(randomSet.insert(1))
print("Current set: ", randomSet.rset)
print(randomSet.remove(2))
print("Current set: ", randomSet.rset)
print(randomSet.insert(2))
print("Current set: ", randomSet.rset)
print(randomSet.getRandom())
print(randomSet.getRandom())
print(randomSet.getRandom())
print(randomSet.getRandom())
print(randomSet.getRandom())
print(randomSet.getRandom())
print(randomSet.getRandom())
print(randomSet.getRandom())
print(randomSet.getRandom())
print(randomSet.getRandom())

print("Current set: ", randomSet.rset)
print(randomSet.remove(1))
print("Current set: ", randomSet.rset)
print(randomSet.insert(2))
print("Current set: ", randomSet.rset)
print(randomSet.getRandom())

