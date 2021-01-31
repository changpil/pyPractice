# Given a list of airline tickets represented by pairs of departure and arrival airports [from, to], reconstruct the itinerary in order. All of the tickets belong to a man who departs from JFK. Thus, the itinerary must begin with JFK.
#
# Note:
#
# If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string. For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
# All airports are represented by three capital letters (IATA code).
# You may assume all tickets form at least one valid itinerary.
# One must use all the tickets once and only once.
# Example 1:
#
# Input: [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
# Output: ["JFK", "MUC", "LHR", "SFO", "SJC"]
# Example 2:
#
# Input: [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
# Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
# Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"].
# But it is larger in lexical order.

import collections
def build_graph(tickets):
    graph = {}
    for ticket in tickets:
        src, dst = ticket[0], ticket[1]
        graph[src] = []
        graph[dst] = []

    for ticket in tickets:
        src, dst = ticket[0], ticket[1]
        graph[src].append(dst)
        graph[src].sort()
    return graph

def findItinerary(tickets):
    graph = build_graph(tickets)
    itin = collections.deque()
    bfs(graph, tickets, "JFK", itin)
    return list(itin)

def bfs(graph, tickets, cur, itin):
    for n in graph[cur]:
        if tickets.count([cur,n]) > 0:
            tickets.remove([cur,n])
            bfs(graph, tickets, n, itin)
    itin.appendleft(cur)

#tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]

# Expected : ["JFK","ATL","JFK","SFO","ATL","SFO"]
tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]


#Expected: ["JFK", "ANU", "EZE", "AXA", "TIA", "ANU", "JFK", "TIA", "ANU", "TIA","JFK"]

tickets = [["EZE","AXA"],["TIA","ANU"],["ANU","JFK"],["JFK","ANU"],["ANU","EZE"],["TIA","ANU"],["AXA","TIA"],["TIA","JFK"],["ANU","TIA"],["JFK","TIA"]]
print(findItinerary(tickets))