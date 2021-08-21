"""
Given an n-ary tree, return the level order traversal of its nodes' values.
Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by
the null value (See examples).

Example 1: VIEW EXAMPLE PIC: n-ary_tree_level_trav_ex1.png
    Input: root = [1,null,3,2,4,null,5,6]
    Output: [[1],[3,2,4],[5,6]]

Example 2: VIEW EXAMPLE PIC: n-ary_tree_level_trav_ex2.png
    Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
    Output: [[1],[2,3,4,5],[6,7,8,9,10],[11,12,13],[14]]

Constraints:
    The height of the n-ary tree is less than or equal to 1000
    The total number of nodes is between [0, 10^4]
"""
from typing import List
from collections import deque


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children



class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        LOT = []
        queue = deque([root])

        if root:
            while queue:
                next_level, level = [], []
                while queue:
                    node = queue.popleft()
                    level.append(node.val)
                    for child in node.children:
                        next_level.append(child)

                queue.extend(next_level)
                LOT.append(level)

        return LOT


if __name__ == "__main__":
    obj = Solution()
    tests = [

    ]

    for t in tests:
        print(t)
        print(obj.levelOrder(t), end="\n\n")
