import collections

n = [2,3,5,2,3,7,8,9]

class FirstUnique:

    def __init__(self, nums):
        self.nums = nums
        self.nums_dict = collections.OrderedDict()

        for key in nums:
            if self.nums_dict.get(key) is None:
                self.nums_dict[key] = True
            else:
                self.nums_dict[key] = False


    def showFirstUnique(self) -> int:
        for key in self.nums_dict:
            if self.nums_dict[key]:
                return key

        return -1

    def add(self, value: int) -> None:
        self.nums.append(value)
        if self.nums_dict.get(value) is None:
            self.nums_dict[value] = True
        else:
            self.nums_dict[value] = False
        #print(self.nums_dict)


# Code for testing
obj = FirstUnique(n)

print(obj.showFirstUnique())
print(obj.add(7))
print(obj.showFirstUnique())
print(obj.add(5))
print(obj.showFirstUnique())
print(obj.add(8))
print(obj.showFirstUnique())

"""dict = collections.OrderedDict()
dict[1] = False
dict[2] = False
dict[3] = False
dict[4] = True
dict[5] = False
dict[6] = True
dict[7] = True

for i in dict:
    if dict[i]:
        print(i)
        break

dict[4] = False

for i in dict:
    if dict[i]:
        print(i)
        break"""
