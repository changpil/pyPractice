#
# accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]
# for e in accounts[0]:
#     for email in e[1:]:
#         print(email)
#
# #print(accounts)
# for e in accounts[0]:
#     print(e)

import collections
def build_graph(nc, prq):
    graph = {}
    for c in range(nc):
        graph[c] = []

    for a in prq:
        src, dst = a[1], a[0]
        graph[src].append(dst)
    return graph

def build_ingress(nc, prq):
    ingress = {}
    for c in range(nc):
        ingress[c] = 0

    for a in prq:
        src, dst = a[1], a[0]
        ingress[dst] = ingress[dst] + 1
    return ingress

def dfs(graph, n, visited, done):
    visited.add(n)
    for nb in graph[n]:
        if nb not in visited:
            if not dfs(graph, nb, visited, done):
                return False
        else:
            if not done[nb]:
                return False
    done[n] = True
    return True

def canFinish(numCourses, prerequisites):
    graph = build_graph(numCourses, prerequisites)
    #ingress = build_ingress(numCourses, prerequisites)
    #print(graph)
    visited, done = set(), {}
    #if all(ingress.values()):
    #    return False

    for i in range(numCourses):
        if i not in visited:
            if not dfs(graph, i, visited, done):
                return False
    return True
# n = 20
# prq = [[0,10],[3,18],[5,5],[6,11],[11,14],[13,1],[15,1],[17,4]]
n= 2
prq = [[0, 1]]
print(canFinish(n, prq))