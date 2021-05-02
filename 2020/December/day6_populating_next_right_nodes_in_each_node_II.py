"""
Given a binary tree
    struct Node {
      int val;
      Node *left;
      Node *right;
      Node *next;
    }
Populate each next pointer to point to its next right node. If there is no next right node, the next
pointer should be set to NULL.
Initially, all next pointers are set to NULL.

Follow up:
    You may only use constant extra space.
    Recursive approach is fine, you may assume implicit stack space does not count as extra space for
    this problem.
Example 1:  VIEW PIC next_right_node_2.png IN DECEMBER FOLDER FOR THIS EXAMPLE
    Input: root = [1,2,3,4,5,null,7]
    Output: [1,#,2,3,#,4,5,7,#]
    Explanation: Given the above binary tree (Figure A), your function should populate each next pointer
    to point to its next right node, just like in Figure B. The serialized output is in level order as
    connected by the next pointers, with '#' signifying the end of each level.

Constraints:
The number of nodes in the given tree is less than 6000.
-100 <= node.val <= 100
"""

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        node_dict = {}

        def add_nodes_to_dict_by_pos(node, place=1):
            if node:
                node_dict[place] = node
                add_nodes_to_dict_by_pos(node.left, place * 2)
                add_nodes_to_dict_by_pos(node.right, (place * 2) + 1)

        add_nodes_to_dict_by_pos(root)

        next_level = 2
        node_places = sorted(node_dict.keys())
        for i in range(len(node_places) - 1):
            if node_places[i + 1] >= next_level:
                next_level *= 2
            else:
                node_dict[node_places[i]].next = node_dict[node_places[i+1]]

        return root


    # This solution is more efficient than the above solution. Uses less space O(1)
    
    def connect2(self, root: 'Node') -> 'Node':
        prev = first = None
        node = root

        while node:
            if node.left:
                if not first:
                    first = node.left
                if prev:
                    prev.next = node.left
                    prev = prev.next
                else:
                    prev = node.left
            if node.right:
                if not first:
                    first = node.right
                if prev:
                    prev.next = node.right
                    prev = prev.next
                else:
                    prev = node.right
            if node.next:
                node = node.next
            else:
                node = first
                first = prev = None

        return root


