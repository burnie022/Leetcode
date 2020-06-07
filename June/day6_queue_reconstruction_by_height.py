"""
Suppose you have a random list of people standing in a queue. Each person is described by a pair of
integers (h, k), where h is the height of the person and k is the number of people in front of this
person who have a height greater than or equal to h. Write an algorithm to reconstruct the queue.
Note:
    The number of people is less than 1,100.
Example:
    Input:
    [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
    Output:
    [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
Hint #1
    What can you say about the position of the shortest person?
    If the position of the shortest person is i, how many people would be in front of the shortest person?
Hint #2
    Once you fix the position of the shortest person, what can you say about the position of the second
    shortest person?
"""


def reconstructQueue(people):
    res = [0 for i in range(len(people))]
    unused_indexes = [i for i in range(len(people))]
    height_dict = {}
    for per in people:
        height_dict[per[0]] = height_dict.get(per[0], []) + [per[1]]

    def reconstruct(h, k):
        nonlocal unused_indexes
        while k:
            index = unused_indexes[k[-1]]
            res[index] = [h, k[-1]]
            unused_indexes = unused_indexes[:k[-1]] + unused_indexes[k[-1]+1:]
            k = k[:-1]

    for sorted_height in sorted(height_dict.keys()):
        reconstruct(sorted_height, sorted(height_dict[sorted_height]))

    return res

"""
Here's a great alternate solution posted by someone on Leetcode, as well as their description:
We first sort the list people, in the order of descending height. If multiple people are of the same
height, sort them in ascending order of the number of people in front of them. For example, if
people = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]], after the line
people_sorted = sorted(people, key = lambda x: (-x[0],x[1])), 
people_sorted = [[7,0], [7,1], [6,1], [5,0], [5,2], [4,4]]. Then for each person [i,j], their index in
people_sorted is larger than or equal to j (due to the way we sort people). Hence to obtain the final
results, we just need to construct an empty list res, and starting from the left, insert each element
[i,j] in people_sorted to position j in res (Latter insertions of [i',j'] won't affect j because either
i' < i, or i' == i and j' > j). The time complexity of the algorithm is O(n^2): We loop over people once,
and each insertion is an O(n) operation. The space complexity is O(n).

We illustrate the above procedure with people_sorted, as i goes from 0 to 5, the empty list res changes
as follows:
[[7,0]] (insert [7,0] at index 0)
[[7,0],[7,1]] (insert [7,1] at index 1)
[[7,0],[6,1],[7,1]] (insert [6,1] at index 1)
[[5,0],[7,0],[6,1],[7,1]] (insert [5,0] at index 0)
[[5,0],[7,0],[5,2],[6,1],[7,1]] (insert [5,2] at index 2)
[[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]] (insert [4,4] at index 4)
"""

def reconstructQueue2(people):
    people = sorted(people, key = lambda x: (-x[0], x[1]))
    # print(people)
    res = []
    for p in people:
        res.insert(p[1], p)
    return res

## End alternate solution


# For testing
p = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

print(reconstructQueue(p))
