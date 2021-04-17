"""
There are a total of n courses you have to take labelled from 0 to n - 1.

Some courses may have prerequisites, for example, if prerequisites[i] = [ai, bi] this means you must take the course bi before the course ai.

Given the total number of courses numCourses and a list of the prerequisite pairs, return the ordering of courses you should take to finish all courses.

If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.



Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].
Example 2:

Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].
"""
import collections
def findOrder(numCourses, prerequisites):
    dependency_list = collections.deque()
    visited = set()
    done = set()
    graph = build_graph(numCourses, prerequisites)
    # startingNodes = getStratingNodes(graph)
    for node in graph:
        # if node not in visited and node in startingNodes:\
        if node not in visited:
            if dfs(graph, node, visited, done, dependency_list) == False:
                return []

    return list(dependency_list)


def build_graph(numCourses, prereq):
    graph = {}
    for course in range(numCourses):
        graph[course] = []
    for dst, src in prereq:
        graph[src].append(dst)
    return graph


# def getStratingNodes(graph):
#     degreeNodes = collections.defaultdict(lambda: 0)
#     for node in graph:
#         degreeNodes[node]
#         for neigh in graph[node]:
#             degreeNodes[neigh] += 1
#     zeroIndegreeNodes = set()
#     for node, NumOfincommingNodes in degreeNodes.items():
#         if NumOfincommingNodes == 0:
#             zeroIndegreeNodes.add(node)
#     return zeroIndegreeNodes


def dfs(graph, node, visited, done, dependency_list):
    visited.add(node)
    # dependency_list.appendleft(node)

    for neig in graph[node]:
        if neig not in visited:
            if not dfs(graph, neig, visited, done, dependency_list):
                return False
        else:
            if neig not in done:
                return False
    dependency_list.appendleft(node)
    done.add(node)
    return True

prerequisites = [[1,0]]
print(findOrder(2, prerequisites)) # So the correct course order is [0,1].

prerequisites = [[1,0],[2,0],[3,1],[3,2]]
print(findOrder(4, prerequisites)) # So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].