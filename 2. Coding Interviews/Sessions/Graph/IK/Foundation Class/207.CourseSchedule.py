"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.



Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take.
To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take.
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
"""

import collections

def canFinish(numCourses, prerequisites):
    dependency_list = collections.deque()
    visited = set()
    done = set()
    graph = build_graph(numCourses, prerequisites)
    #startingNodes = getStratingNodes(graph)
    for node in graph:
        #if node not in visited and node in startingNodes:
        if node not in visited:
            if dfs(graph, node, visited, done) == False:
                return False

    return True

def build_graph(numCourses, prereq):
    graph = {}
    for course in range(numCourses):
        graph[course] = []
    for src, dst in prereq:
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

def dfs(graph, node, visited, done):
    visited.add(node)
    for neig in graph[node]:
        if neig not in visited:
            if dfs(graph, neig, visited, done) == False:
                return False
        else:
            if neig not in done:
                return False
    done.add(node)
    return True

prerequisites = [[1,0]]
print(canFinish(2, prerequisites))


prerequisites = [[1,0],[0,1]]
print(canFinish(2, prerequisites))


# Need to check cyclic
prerequisites = [[1,0],[0,2], [2, 0]]
print(canFinish(3, prerequisites))