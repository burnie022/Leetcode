"""
In this problem, a tree is an undirected graph that is connected and has no cycles.

You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added. The
added edge has two different vertices chosen from 1 to n, and was not an edge that already existed. The graph is
represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge between nodes ai
and bi in the graph.

Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple answers,
return the answer that occurs last in the input.

Example 1: VIEW PIC: reduntant_conn_ex1.jpg
    Input: edges = [[1,2],[1,3],[2,3]]
    Output: [2,3]

Example 2: VIEW PIC: reduntant_conn_ex2.jpg
    Input: edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
    Output: [1,4]

Constraints:
    n == edges.length
    3 <= n <= 1000
    edges[i].length == 2
    1 <= ai < bi <= edges.length
    ai != bi
    There are no repeated edges.
    The given graph is connected.
"""
from typing import List


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        map = {}
        for a, b in edges:
            map[a] = map.get(a, []) + [b]
            map[b] = map.get(b, []) + [a]

        seen, cycle, stack, came_from = {edges[0][0]}, [], [edges[0][0]], [0]
        while stack:
            if map[stack[-1]] and map[stack[-1]][-1] == came_from[-1]:
                map[stack[-1]].pop()

            if map[stack[-1]]:
                if map[stack[-1]][-1] not in seen:
                    stack.append(map[stack[-1]].pop())
                    seen.add(stack[-1])
                    came_from.append(stack[-2])
                else:
                    cycle.append(map[stack[-1]][-1])
                    while stack and stack[-1] != cycle[0]:
                        cycle.append(stack.pop())
                    break
            else:
                stack.pop()
                came_from.pop()

        cycle = set(cycle)
        last = []
        for a, b in edges:
            if a in cycle and b in cycle:
                last = [a, b]

        return last



if __name__ == "__main__":
    obj = Solution()
    tests = [
        [[1, 2], [1, 3], [2, 3]],
        [[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]],
        [[1, 2], [1, 4], [2, 3], [3, 4], [1, 5]],
        [[1, 2], [1, 3], [2, 3], [3, 4]],
        [[1, 2], [1, 3], [2, 3], [3, 4], [3, 5]],
        [[1, 2], [1, 3], [2, 3], [3, 4], [3, 5], [4, 6]],
        [[1, 2], [1, 3], [2, 3], [3, 4], [3, 5], [4, 6], [6, 7]],
        [[5, 8], [1, 2], [1, 3], [2, 3], [3, 4], [3, 5], [4, 6], [6, 7]],

    ]

    for t in tests:
        print(t)
        print(obj.findRedundantConnection(t), end="\n\n")
