l1 = []
l2 = []
l3 = []
h = {
        'Arad':366,
        'Zerid':374,
        'Oradea':380,
        'Sibiu':253,
        'Fagaras':176,
        'Bucharest':0,
        'Rimicu':193,
        'Pitesti':100
    }

graph = {
            'Arad':['Zerid','Sibiu'],
            'Zerid':['Arad','Oradea'],
            'Oradea':['Zerid','Sibiu'],
            'Sibiu':['Arad','Oradea','Fagaras','Rimicu'],
            'Fagaras':['Sibiu','Bucharest'],
            'Bucharest':['Fagaras','Pitesti'],
            'Rimicu':['Sibiu','Pitesti'],
            'Pitesti':['Bucharest','Rimicu']
        }

g = {
        'Arad':[75,140],
        'Zerid':[75,71],
        'Oradea':[71,151],
        'Sibiu':[140,151,99,88],
        'Fagaras':[99,211],
        'Bucharest':[211,101],
        'Rimicu':[80,97],
        'Pitesti':[101,97]
    }

def AStar(src, dest, x, l1, l2, l3):
    if src == dest:
        print("Destination reached")
        return True
    else:
        for i in range(0, len(g[src])):
            l2.append(graph[src][i])
            l1.append(x+g[src][i]+h[graph[src][i]])
            l3.append(g[src][i]+x)
            print(l1,l2,l3)
        temp = l2[l1.index(min(l1))]
        x = l3[l1.index(min(l1))]
        print(l1.index(min(l1)),temp,x)
        l2.remove(temp)
        l1.pop(l1.index(min(l1)))
        l3.remove(x)
        print(l1, l2, l3)
        print()
        return AStar(temp, dest, x, l1, l2, l3)

AStar('Arad','Bucharest',0,l1,l2,l3)
