"""
Given an array w of positive integers, where w[i] describes the weight of index i, write a function pickIndex which
randomly picks an index in proportion to its weight.
Note:
    1 <= w.length <= 10000
    1 <= w[i] <= 10^5
    pickIndex will be called at most 10000 times.
Example 1:
    Input:
    ["Solution","pickIndex"]
    [[[1]],[]]
    Output: [null,0]
Example 2:
    Input:
    ["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
    [[[1,3]],[],[],[],[],[]]
    Output: [null,0,1,1,1,0]
Explanation of Input Syntax:
The input is two lists: the subroutines called and their arguments. Solution's constructor has one argument, the
array w. pickIndex has no arguments. Arguments are always wrapped with a list, even if there aren't any.
"""

import random
import bisect

class Solution:

    def __init__(self, w):
        self.w = [w[0]]
        for i in range(1,len(w)):
            self.w.append(w[i] + self.w[-1])
        print(self.w)

    def pickIndex(self) -> int:
        r = random.randint(1, self.w[-1])
        print("r:",r)
        return bisect.bisect_left(self.w, r)


# for testing

w = [1,5,2]
obj = Solution(w)
for i in range(8):
    print(obj.pickIndex())

