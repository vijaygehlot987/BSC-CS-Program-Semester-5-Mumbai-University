graph={
    "S" : ["A", "B", "C"],
    "A" : ["B", "D", "S"],
    "B" : ["A", "S", "D", "H"],
    "C" : ["S", "L"],
    "D" : ["A", "F", "B"],
    "E" : ["G", "K"],
    "F" : ["D", "H"],
    "G" : ["H", "E"],
    "H" : ["B", "F", "G"],
    "I" : ["L", "K"],
    "J" : ["L", "K"],
    "K" : ["I", "J", "E"],
    "L" : ["C", "I", "J"]
    }
def dfs(graph,dest,src,tree):
    if (src not in tree and src!=tree):
        tree.append(src)
        for i in graph[src]:
            dfs(graph,dest,i,tree)
    return tree
x=input("src")
y=input("dest")
print(dfs(graph,y,x,[]))
