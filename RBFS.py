"""
Node ---> [f(n), totalPathCost, node, via]

"""
import heapq
def RBFS(graph, heuristic, start, goal, fLimit):
    print(start, fLimit)
    if start[2] == goal:
        return start[1], 0
    child = []
    for node, weight in graph[start[2]]:
        print("Expanding : ", node)
        child.append([heuristic[node] + weight + start[1], weight + start[1], node, start[2]])
        
    if not child : return False, 10000

##    for c in child:
##        c[0] = max(c[0] + c[1], start[0])

    while True:
        child.sort()
        best = child[0]
        alt = child[1][0]
        if best[0] > fLimit : return False, best[0]
        print("Selecting :", best[2])
        print("Alt :", alt)
        result, best[0] = RBFS(graph, heuristic, best, goal, min(best[0], alt))
        if result != False : return result, 0

def build_graph_weighted(file):
    """Builds a weighted, undirected graph"""
    graph = {}
    for line in file:
        v1, v2, w = line.split(',')
        v1, v2 = v1.strip(), v2.strip()
        w = int(w.strip())
        if v1 not in graph:
            graph[v1] = []
        if v2 not in graph:
            graph[v2] = []
        graph[v1].append((v2,w))
        graph[v2].append((v1,w))
    return graph

def build_heuristic_dict():
    h = {}
    with open("hueristic.txt", 'r') as file:
        for line in file:
            line = line.strip().split(",")
            node = line[0].strip()
            sld = int(line[1].strip())
            h[node] = sld
    return h

with open('graph.txt', 'r') as file:
    lines = file.readlines()

start = lines[1].strip()
end = lines[2].strip()
g = build_graph_weighted(lines[4:])
h = build_heuristic_dict()
print(start)
print(end)

print("Path from", start, "to", end, ":", RBFS(g, h, [h[start], 0, start, start], end, 10000))

    

    
    
    
