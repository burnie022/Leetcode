"""
There are n cities connected by m flights. Each flight starts from city u and arrives at v with a price w.
Now given all the cities and flights, together with starting city src and the destination dst, your task is to
find the cheapest price from src to dst with up to k stops. If there is no such route, output -1.
Example 1:
    Input:
    n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
    src = 0, dst = 2, k = 1
    Output: 200
    Explanation:
    The graph looks like this:
            0
          /   \
    100 /      \ 500
      /         \
     1 --------- 2
         100

    The cheapest price from city 0 to city 2 with at most 1 stop costs 200, as marked red in the picture.

Example 2:
    Input:
    n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
    src = 0, dst = 2, k = 0
    Output: 500
    Explanation:
    The graph looks like this:
            0
          /   \
    100 /      \ 500
      /         \
     1 --------- 2
         100

    The cheapest price from city 0 to city 2 with at most 0 stop costs 500, as marked blue in the picture.

Constraints:
    The number of nodes n will be in range [1, 100], with nodes labeled from 0 to n - 1.
    The size of flights will be in range [0, n * (n - 1) / 2].
    The format of each flight will be (src, dst, price).
    The price of each flight will be in the range [1, 10000].
    k is in the range of [0, n - 1].
    There will not be any duplicated flights or self cycles.
"""


def findCheapestPrice(n: int, flights, src: int, dst: int, K: int) -> int:
    map = {}
    trip_costs = {}
    """# cost_from_node will be tuples in the form of "node:(k, cost)" where k is the number of stops between the
    # node and dst, and cost is the total cost of paths in between
    cost_from_node = {} """
    totals = set()

    for a, b, cost in flights:
        map[a] = map.get(a, []) + [b]
        trip_costs[(a,b)] = cost

    # print(map)
    # print(trip_costs)

    def dfs(start, cost=0, k_remaining=K):
        # print("start is: ", start)
        # print("k_remaining: ", k_remaining)
        if start == dst:
            totals.add(cost)
            return
        if k_remaining < 0:
            return

        for dest in map.get(start, []):
            dfs(dest, cost + trip_costs[(start, dest)], k_remaining - 1)

    dfs(src)

    return min(totals) if totals else -1


"""
Study the below code, by a user on L"""
import collections
import heapq

def findCheapestPriceDijkstra(n, flights, src, dst, K):
    """
    :type n: int
    :type flights: List[List[int]]
    :type src: int
    :type dst: int
    :type K: int
    :rtype: int
    """
    map = collections.defaultdict(dict)
    for a, b, cost in flights:
        map[a][b] = cost
    pq = [(0, src, -1)]

    while pq:
        cost, s, k = heapq.heappop(pq)
        if s == dst:
            return cost
        if k < K:
            for t in map[s]:
                heapq.heappush(pq, (cost + map[s][t], t, k + 1))
    return -1



# For testing
n = 3
e = [[0,1,100],[1,2,100],[0,2,500]]
src = 0
dst = 2
k = 1
# print("Minimum cost: ", findCheapestPrice(n, e, src, dst, k))

print("Minimum cost: ", findCheapestPriceDijkstra(n, e, src, dst, k))


"""
n = 17
edges = [[0,12,28],[5,6,39],[8,6,59],[13,15,7],[13,12,38],[10,12,35],[15,3,23],[7,11,26],[9,4,65],[10,2,38],[4,7,7],[14,15,31],[2,12,44],[8,10,34],[13,6,29],[5,14,89],[11,16,13],[7,3,46],[10,15,19],[12,4,58],[13,16,11],[16,4,76],[2,0,12],[15,0,22],[16,12,13],[7,1,29],[7,14,100],[16,1,14],[9,6,74],[11,1,73],[2,11,60],[10,11,85],[2,5,49],[3,4,17],[4,9,77],[16,3,47],[15,6,78],[14,1,90],[10,5,95],[1,11,30],[11,0,37],[10,4,86],[0,8,57],[6,14,68],[16,8,3],[13,0,65],[2,13,6],[5,13,5],[8,11,31],[6,10,20],[6,2,33],[9,1,3],[14,9,58],[12,3,19],[11,2,74],[12,14,48],[16,11,100],[3,12,38],[12,13,77],[10,9,99],[15,13,98],[15,12,71],[1,4,28],[7,0,83],[3,5,100],[8,9,14],[15,11,57],[3,6,65],[1,3,45],[14,7,74],[2,10,39],[4,8,73],[13,5,77],[10,0,43],[12,9,92],[8,2,26],[1,7,7],[9,12,10],[13,11,64],[8,13,80],[6,12,74],[9,7,35],[0,15,48],[3,7,87],[16,9,42],[5,16,64],[4,5,65],[15,14,70],[12,0,13],[16,14,52],[3,10,80],[14,11,85],[15,2,77],[4,11,19],[2,7,49],[10,7,78],[14,6,84],[13,7,50],[11,6,75],[5,10,46],[13,8,43],[9,10,49],[7,12,64],[0,10,76],[5,9,77],[8,3,28],[11,9,28],[12,16,87],[12,6,24],[9,15,94],[5,7,77],[4,10,18],[7,2,11],[9,5,41]]
src = 13
dest = 4
K= 13
"""