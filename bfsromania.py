graph={1:[2,3],
       2:[1,4,5],
       3:[1,6,4],
       4:[2,3,6],
       5:[2,6],
       6:[3,4,5]}
visited=[]
queue=[]
def bfs(graph,src,dest):
    if src not in visited:
        visited.append(src)
        if src in queue:
            queue.remove(src)
    for i in graph[src]:
        if i not in visited and i not in queue:
            queue.append(i)
    for i in queue:
	if dest not in visited:
	 src=i
         bfs(graph,src,dest)
        else:
         break
bfs(graph,1,4)
print(visited)       
       
