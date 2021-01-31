import collections
import math

import collections
import math



def shortestAlternatingPaths(n, red_edges, blue_edges):
    counts = {i: -1 for i in range(n)}
    counts[0] = 0
    visited = {}
    visited[(-1, 0, "red")] = 0
    visited[(-1, 0, "blue")] = 0
    queue = collections.deque()
    queue.append((-1, 0, None))
    visited[(-1, 0, None)] = 0
    while queue:
        prevN, curN, prevColor = queue.popleft()

        for nextN in range(n):
            # if curN == nextN:
            #    continue

            # previousColor = blue/None and nextColor == red
            if (prevColor == "blue" or prevColor == None) and (curN, nextN, "red") not in visited and [curN,
                                                                                                       nextN] in red_edges:
                queue.append((curN, nextN, "red"))
                if counts[nextN] == -1:
                    counts[nextN] = visited[(prevN, curN, "blue")] + 1
                visited[(curN, nextN, "red")] = visited[(prevN, curN, "blue")] + 1
            # previousColor = red/None and nextColor == blue
            if (prevColor == "red" or prevColor == None) and (curN, nextN, "blue") not in visited and [curN,
                                                                                                       nextN] in blue_edges:
                queue.append((curN, nextN, "blue"))

                if counts[nextN] == -1:
                    counts[nextN] = visited[(prevN, curN, "red")] + 1
                visited[(curN, nextN, "blue")] = visited[(prevN, curN, "red")] + 1

    rev = []
    for i in range(n):
        rev.append(counts[i])
    return rev


n = 3
red = [[0,1],[0,2]]
blue = [[1,0]]
print(shortestAlternatingPaths(n, red, blue))


n = 6
red = [[4,1],[3,5],[5,2],[1,4],[4,2],[0,0],[2,0],[1,1]]
blue = [[5,5],[5,0],[4,4],[0,3],[1,0]]
# Expected [0,-1,4,1,-1,2]
print(shortestAlternatingPaths(n, red, blue))