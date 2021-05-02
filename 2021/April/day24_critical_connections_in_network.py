"""
There are n servers numbered from 0 to n-1 connected by undirected server-to-server connections forming a network
where connections[i] = [a, b] represents a connection between servers a and b. Any server can reach any other
server directly or indirectly through the network.
A critical connection is a connection that, if removed, will make some server unable to reach some other server.
Return all critical connections in the network in any order.

Example 1:
    VIEW EXAMPLE PIC: crit_conn_network_ex1.png
    Input: n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
    Output: [[1,3]]
    Explanation: [[3,1]] is also accepted.

Constraints:
    1 <= n <= 10^5
    n-1 <= connections.length <= 10^5
    connections[i][0] != connections[i][1]
    There are no repeated connections.
Hint:
    Use Tarjan's algorithm.
"""
from typing import List
from collections import deque


# Tarjan's Algorithm O(V + E) optimal solution (vertices + edges). Uses DFS.
class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        self.graph = {}
        self.next_id = 0
        self.node_id = {}
        self.node_low = {}
        self.critical_connections = []

        for a, b in connections:
            self.graph[a] = self.graph.get(a, []) + [b]
            self.graph[b] = self.graph.get(b, []) + [a]

        self.tarjans_algorithm_dfs()

        return self.critical_connections


    def tarjans_algorithm_dfs(self, curr_node=0, parent=None):
        self.node_id[curr_node] = self.next_id
        self.node_low[curr_node] = self.next_id
        self.next_id += 1

        for neighbor in self.graph[curr_node]:
            if neighbor != parent:
                if neighbor not in self.node_id:
                    self.tarjans_algorithm_dfs(neighbor, curr_node)

                if self.node_low[neighbor] > self.node_id[curr_node]:
                    self.critical_connections.append([curr_node, neighbor])
                elif self.node_low[neighbor] < self.node_low[curr_node]:
                    self.node_low[curr_node] = self.node_low[neighbor]



# Suboptimal solution that takes too much time. Uses BFS
class BruteForceSolution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        network_map = {}
        for i in range(n):
            network_map[i] = set()
        for a, b in connections:
            network_map[a].add(b)
            network_map[b].add(a)

        return self.find_critical_connections(n, connections, network_map)


    def find_critical_connections(self, n, connections, network_map):
        critical_connections = []
        for a, b in connections:
            network_map[a].remove(b)
            is_critical = self.critical_connection_dfs(network_map, a, b)
            if is_critical:
                critical_connections.append([a, b])
            network_map[a].add(b)

        return critical_connections


    def critical_connection_dfs(self, network_map, start, target):
        seen = set()
        queue = deque()
        queue.append(start)

        while queue:
            curr_node = queue.popleft()
            seen.add(curr_node)
            for node in network_map[curr_node]:
                if node in seen:
                    continue
                if node == target:
                    return False
                queue.append(node)

        return True


# For testing

obj = Solution()
tests = [
    (4, [[0,1],[1,2],[2,0],[1,3]]),
    (10, [[0,1],[1,2],[2,3],[3,4],[4,5],[5,1],[2,6],[6,7],[7,8],[6,8],[8,9]])
]

for n, c in tests:
    print(n)
    print(c)
    print(obj.criticalConnections(n, c), end="\n\n")
