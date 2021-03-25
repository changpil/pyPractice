# def trace_path(planes):
#     for departure in planes:
#         result = []
#         visited = set()
#         while planes.get(departure, None):
#             result.append([departure, planes[departure]])
#             visited.add(departure)
#             departure = planes[departure]
#
#             if len(visited) == len(planes):
#                 return result
#     return None

import collections
def bfs(planes, state):
    result = []
    visited = set()
    queue = collections.deque()
    queue.append(state)
    visited.add(state)
    while queue:
        source = queue.pop()
        destination = planes[source] if source in planes else None
        if destination and destination not in visited:
            result.append([source, destination])
            visited.add(destination)
            queue.append(destination)
    return result

def airportTrace(planes):
    for state in planes:
        result = bfs(planes, state)
        if len(result) == len(planes):
            return result
    return None

planes = {
  "NewYork": "Chicago",
  "Boston": "Texas",
  "Missouri": "NewYork",
  "Texas": "Missouri",
 # "Seattle": "Chicago",
  "Chicago": "Seattle"
}

# print(trace_path(planes))
print(airportTrace(planes))