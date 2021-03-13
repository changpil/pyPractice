# Critical Connections
# Given a network of servers where each server is connected to every other server directly or indirectly through the bidirectional connections in the network,
# find all the critical connections.
# A connection in a connected network is said to be critical if removing it disconnects the network.



def build_graph(number_of_servers, connections):
    graph = {}

    for i in range(number_of_servers):
        graph[i] = []

    for e in connections:
        s, e = e[0],  e[1]
        graph[s].append(e)
        graph[e].append(s)
    return graph

# Brute Force way. Time exceeded
# def find_critical_connections(number_of_servers, connections):
#
#     graph = None
#     critical_network = []
#     visited= set()
#     for i in range(len(connections)):
#         visited.clear()
#         graph = build_graph(number_of_servers, connections[:i] + connections[i+1:])
#         bfs(graph, 0, visited)
#         if len(visited) != number_of_servers:
#             critical_network.append(connections[i])
#     if critical_network:
#         return critical_network
#     return [[-1,-1]]
#
# def bfs(graph, v, visited):
#     visited.add(v)
#     for neb in graph[v]:
#         if neb not in visited:
#             bfs(graph, neb, visited)



def find_critical_connections(number_of_servers, connections):
    graph = build_graph(number_of_servers, connections)
    critical_network, visited, ts, discoveryTime, backEdgeTime = [], set(), [0], dict(), dict()
    for i in range(number_of_servers):
        if i not in visited:
            dfs(graph, i, None, visited, ts, discoveryTime, backEdgeTime, critical_network)
    if not critical_network:
        return [[-1, -1]]
    return critical_network


def dfs(graph, n, p, visited, ts, discoveryTime, backEdgeTime, critical_network):
    time = ts[0]
    visited.add(n)
    discoveryTime[n] = backEdgeTime[n] = time
    time += 1
    ts[0] = time
    for child in graph[n]:
        if child == p:
            continue
        if child not in visited:
            dfs(graph, child, n, visited, ts, discoveryTime, backEdgeTime, critical_network)
            if discoveryTime[n] < backEdgeTime[child]:
                critical_network.append([n, child])
            backEdgeTime[n] = min(backEdgeTime[n], backEdgeTime[child])
        else:
            backEdgeTime[n] = min(discoveryTime[child], backEdgeTime[n])

# [[0, 4], [1, 3]]
connections = [[0, 1], [0, 2], [0, 4], [1, 2], [1, 3]]
print(find_critical_connections(5, connections))

#[[-1, -1]]
connections = [[0, 1],[0, 2],[0, 3],[1, 2],[2, 3]]
print(find_critical_connections(4, connections))

# [[3, 1], [3, 4]]
connections =[[0, 1], [1, 2], [0, 2], [5, 4], [4, 6], [6, 5], [3, 1], [3, 4]]
print(find_critical_connections(7, connections))