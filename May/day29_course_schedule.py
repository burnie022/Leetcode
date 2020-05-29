"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses-1.
Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is
expressed as a pair: [0,1]
Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all
courses?
Example 1:
    Input: numCourses = 2, prerequisites = [[1,0]]
    Output: true
    Explanation: There are a total of 2 courses to take.
                 To take course 1 you should have finished course 0. So it is possible.
Example 2:
    Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
    Output: false
    Explanation: There are a total of 2 courses to take.
                 To take course 1 you should have finished course 0, and to take course 0 you should
                 also have finished course 1. So it is impossible.
Constraints:
    The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more
    about how a graph is represented.
    You may assume that there are no duplicate edges in the input prerequisites.
    1 <= numCourses <= 10^5
Hint #1
This problem is equivalent to finding if a cycle exists in a directed graph. If a cycle exists, no topological
ordering exists and therefore it will be impossible to take all courses.
Hint #2
Topological Sort via DFS - A great video tutorial (21 minutes) on Coursera explaining the basic concepts of
Topological Sort.
Hint #3
Topological sort could also be done via BFS.
"""
def canFinish(numCourses, prerequisites) -> bool:
    dict_prereq = {}
    confirmed = []
    for course1, course2 in prerequisites:
        dict_prereq[course1] = dict_prereq.get(course1, []) + [course2]

    if numCourses == len(dict_prereq.keys()):
        return False

    confirmed = [course for course in range(numCourses) if course not in dict_prereq.keys()]
    # print(dict_prereq)
    # print("Confirmed:", confirmed)

    confirmed = set(confirmed)

    def dfs(node, checked_nodes):
        if node in confirmed:
            return True
        if node in checked_nodes:
            print("met start course", node)
            return False
        for course in dict_prereq.get(node):
            checked_nodes.add(node)
            if not dfs(course, checked_nodes):
                return False
        confirmed.add(node)
        return True

    for course in dict_prereq.keys():
        if not course in confirmed:
            if not all(dfs(c, {course}) for c in dict_prereq[course]):
                return False
            else:
                confirmed.add(course)

    return True




# For testing
tests = [(4,  [[0,1],[1,2],[2,1]]),
         (2, [[0,1]]),
         (2, [[0,1], [1,0]]),
         (7, [[1,0],[0,3],[0,2],[3,2],[2,5],[4,5],[5,6],[2,4]])]

for n, c in tests:
    print(n,",",c,":", canFinish(n, c))


