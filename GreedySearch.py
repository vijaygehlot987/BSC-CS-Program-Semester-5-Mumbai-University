l1 = []
valid = []
h = {
        'Arad':266,
        'Zerid':314,
        'Oradea':200,
        'Sibiu':256,
        'Fagaras':77,
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

def GreedySearch(src, dest):
    if src not in valid:
        valid.append(src)
        if src == dest:
            print("You have reached the city")
            return True
        else:
            l = []
            l1 = []
            for i in graph[src]:
                l.append(h[i])
                l1.append(i)
            print(l1)
            print(l)
            print(min(l),l1[l.index(min(l))])
            temp = l1[l.index(min(l))]
            return GreedySearch(temp, dest)
        print("Destination not reached")

src = input("Enter the source")
dest = input("Enter the destination")
print(src)
GreedySearch(src, dest)
