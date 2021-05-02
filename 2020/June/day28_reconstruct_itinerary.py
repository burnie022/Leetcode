"""
Given a list of airline tickets represented by pairs of departure and arrival airports [from, to], reconstruct the
itinerary in order. All of the tickets belong to a man who departs from JFK. Thus, the itinerary must begin with JFK.
Note:
If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read
as a single string. For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
All airports are represented by three capital letters (IATA code).
You may assume all tickets form at least one valid itinerary.
One must use all the tickets once and only once.
Example 1:
    Input: [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
    Output: ["JFK", "MUC", "LHR", "SFO", "SJC"]
Example 2:
    Input: [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
    Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
    Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"].
             But it is larger in lexical order.
"""

def findItinerary(tickets):
    itinerary = ["JFK"]
    map = {}
    for origin, dest in tickets:
        map[origin] = map.get(origin, []) + [dest]

    for key in map:
        map[key] = sorted(map[key])

    def dfs(start):
        cities = map.get(start, [])
        if not cities:
            if len(itinerary) == len(tickets) + 1:
                return True
            else:
                return False

        for city in cities:
            map[start] = map[start][1:]
            itinerary.append(city)

            if dfs(city):
                return True
            else:
                itinerary.pop()
                map[start].append(city)

        return False

    dfs("JFK")

    return itinerary


# For testing
tests = ([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]],
    [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]],
    [["MUC", "LHR"], ["JFK", "MUC"]],
    [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]],
[["EZE","TIA"],["EZE","HBA"],["AXA","TIA"],["JFK","AXA"],["ANU","JFK"],["ADL","ANU"],["TIA","AUA"],["ANU","AUA"],["ADL","EZE"],["ADL","EZE"],["EZE","ADL"],["AXA","EZE"],["AUA","AXA"],["JFK","AXA"],["AXA","AUA"],["AUA","ADL"],["ANU","EZE"],["TIA","ADL"],["EZE","ANU"],["AUA","ANU"]]

         )

for t in tests:
    print(findItinerary(t))


"""
Input: [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]
my output: ["JFK","KUL"]
expected: ["JFK","NRT","JFK","KUL"]


input: 
[["EZE","TIA"],["EZE","HBA"],["AXA","TIA"],["JFK","AXA"],["ANU","JFK"],["ADL","ANU"],["TIA","AUA"],["ANU","AUA"],["ADL","EZE"],["ADL","EZE"],["EZE","ADL"],["AXA","EZE"],["AUA","AXA"],["JFK","AXA"],["AXA","AUA"],["AUA","ADL"],["ANU","EZE"],["TIA","ADL"],["EZE","ANU"],["AUA","ANU"]]
output: ["JFK"]
expected: ["JFK","AXA","AUA","ADL","ANU","AUA","ANU","EZE","ADL","EZE","ANU","JFK","AXA","EZE","TIA","AUA","AXA","TIA","ADL","EZE","HBA"]

"""

