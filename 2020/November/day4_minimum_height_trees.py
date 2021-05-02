"""
A tree is an undirected graph in which any two vertices are connected by exactly one path.
In other words, any connected graph without simple cycles is a tree.

Given a tree of n nodes labelled from 0 to n - 1, and an array of n - 1 edges where
edges[i] = [ai, bi] indicates that there is an undirected edge between the two nodes ai
and bi in the tree, you can choose any node of the tree as the root. When you select a
node x as the root, the result tree has height h. Among all possible rooted trees, those
with minimum height (i.e. min(h))  are called minimum height trees (MHTs).

Return a list of all MHTs' root labels. You can return the answer in any order.

The height of a rooted tree is the number of edges on the longest downward path between the root and a leaf.

Example 1:
    Input: n = 4, edges = [[1,0],[1,2],[1,3]]
    Output: [1]
    Explanation: As shown, the height of the tree is 1 when the root is the node with label 1 which is the only MHT.

Example 2:
    Input: n = 6, edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
    Output: [3,4]

Example 3:
    Input: n = 1, edges = []
    Output: [0]

Example 4:
    Input: n = 2, edges = [[0,1]]
    Output: [0,1]

Constraints:
    1 <= n <= 2 * 104
    edges.length == n - 1
    0 <= ai, bi < n
    ai != bi
    All the pairs (ai, bi) are distinct.
    The given input is guaranteed to be a tree and there will be no repeated edges.
Hint:
    How many MHTs can a graph have at most?
"""
# from collections import Counter

# Brute force solution. Works but too long runtime
def findMinHeightTrees2(n: int, edges):
    print("")
    if not edges:
        return [0]
    if len(edges) == 1:
        return edges[0]

    map = {}
    for a, b in edges:
        map[a] = map.get(a, []) + [b]
        map[b] = map.get(b, []) + [a]

    # print(map)
    def dfs(node, visited):
        if node in visited:
            return 0
        visited.add(node)
        count = 0
        for dest in map[node]:
            count = max(count, dfs(dest, visited))

        return 1 + count

    tot_edges = {}
    min_edges = 200000
    for edge in map.keys():
        tot_edges[edge] = dfs(edge, set()) - 1
        min_edges = min(tot_edges[edge], min_edges)

    print(min_edges)
    print(tot_edges)

    return [edge for edge in tot_edges.keys() if tot_edges[edge] == min_edges]



"""
THE SOLUTION BELOW WORKS! iT FIRST FINDS THE TREES LEAVES AND REMOVES THEM CONTINUOUSLY UNTIL <= 2 NODES
ARE LEFT IN THE TREE. THESE ARE THE NODES THAT ARE RETURNED
"""

def findMinHeightTrees5(n: int, edges):
    print("")
    if not edges:
        return [0]
    if len(edges) == 1:
        return edges[0]

    keys_left = set([i for i in range(n)])
    graph = {}
    for a, b in edges:
        if not graph.get(a):
            graph[a] = set()
        if not graph.get(b):
            graph[b] = set()
        graph[a].add(b)
        graph[b].add(a)

    def find_leaves(graph):
        leaves = set()
        for leaf in graph.keys():
            if len(graph[leaf]) == 1:
                leaves.add(leaf)
        return leaves

    def trim_leaves(leaves):
        new_leaves = set()
        for leaf in leaves:
            for connecting_leaf in graph[leaf]:
                graph[connecting_leaf].remove(leaf)
            if len(graph[connecting_leaf]) == 1:
                new_leaves.add(connecting_leaf)
        keys_left.difference_update(leaves)
        return new_leaves

    leaves = find_leaves(graph)

    while len(keys_left) > 2:
        leaves = trim_leaves(leaves)

    return list(keys_left)





# Test cases

tests = [(6, [[3,0],[3,1],[3,2],[3,4],[5,4]]),
         (4, [[1,0],[1,2],[1,3]]),
         (1, []),
         (2, [[0, 1]]),
         (5, [[0,2],[2,1],[2,3],[3,4]]),
         (7, [[0,1],[1,2],[1,4],[2,3],[0,5],[5,6]]),
         (11, [[0,1],[1,2],[1,4],[2,3],[0,5],[5,6],[3,7],[3,8],[3,10],[8,9]])

         ]

for n, e in tests:
    print(findMinHeightTrees5(n, e))

