ww = [['Start','Breeze','PIT','Breeze'],
      ['Stench','Unknown','Breeze','Unknown'],
      ['Wumpus','Gold','PIT','Breeze'],
      ['Stench','Unknown','Breeze','PIT']
     ]

actions = [['left',''],['right',''],['up',''],['down','']]
check = [['NOT OK','NOT OK','NOT OK','NOT OK'],
         ['NOT OK','NOT OK','NOT OK','NOT OK'],
         ['NOT OK','NOT OK','NOT OK','NOT OK'],
         ['NOT OK','NOT OK','NOT OK','NOT OK']
        ]
explored = []
def moves(i,j):
    si = i
    sj = j
    r = j+1
    l = j-1
    u = i-1
    d = i+1
    if i is 0 and j is 0:
        actions[0][0] = ''
        actions[0][1] = ''
        actions[1][0] = si
        actions[1][1] = r
        actions[2][0] = ''
        actions[2][1] = ''
        actions[3][0] = d
        actions[3][1] = sj
        print(actions)
    elif i is 0 and j is 3:
        actions[0][0] = si
        actions[0][1] = l
        actions[1][0] = ''
        actions[1][1] = ''
        actions[2][0] = ''
        actions[2][1] = ''
        actions[3][0] = d
        actions[3][1] = sj
        print(actions)
    elif i is 3 and j is 0:
        actions[0] = ''
        actions[1][0] = si
        actions[1][1] = r
        actions[2][0] = u
        actions[2][1] = sj
        actions[3] = ''
        print(actions)
    elif i is 3 and j is 3:
        actions[0][0] = si
        actions[0][1] = l
        actions[1] = ''
        actions[2][0] = u
        actions[2][1] = sj
        actions[3] = ''
        print(actions)
    elif i is 0:
        actions[0][0] = si
        actions[0][1] = l
        actions[1][0] = si
        actions[1][1] = r
        actions[2][0] = ''
        actions[2][1] = ''
        actions[3][0] = d
        actions[3][1] = sj
        print(actions)
    elif i is 3:
        actions[0][0] = si
        actions[0][1] = l
        actions[1][0] = si
        actions[1][1] = r
        actions[2][0] = u
        actions[2][1] = sj
        actions[3] = ''
        print(actions)
    elif j is 0:
        actions[0][0] = ''
        actions[0][1] = ''
        actions[1][0] = si
        actions[1][1] = r
        actions[2][0] = u
        actions[2][1] = sj
        actions[3][0] = d
        actions[3][1] = sj
        print(actions)
    elif j is 3:
        actions[0][0] = si
        actions[0][1] = l
        actions[1] = ''
        actions[2][0] = u
        actions[2][1] = sj
        actions[3][0] = d
        actions[3][1] = sj
        print(actions)
    else:
        actions[0][0] = si
        actions[0][1] = l
        actions[1][0] = si
        actions[1][1] = r
        actions[2][0] = u
        actions[2][1] = sj
        actions[3][0] = d
        actions[3][1] = sj
        print(actions)

def WumpusAlgo(i,j):
    while True:
        agent = ww[i][j]
        if agent is 'Gold':
            print("You have found the gold")
            exit()
            
        if agent is 'Start':
            percepts = []
            coordinates = []
            check[i][j] = 'OK'
            moves(i, j)
            for k in range(0,4):
                if actions[k][0]!='':
                    percepts.append(ww[actions[k][0]][actions[k][1]])
                    coordinates.append(actions[k])
            print(percepts)
            print(coordinates)
            for k in range(len(percepts)):
                b = []
                if(percepts[k] == 'Gold'):
                    b = coordinates[k]
                    agent = ww[b[0]][b[1]]
                    if agent not in explored:
                        print(agent)
                        WumpusAlgo(b[0],b[1])
                if(percepts[k] != 'PIT' and percepts[k] != 'Wumpus'):
                    if(percepts[k] == 'Breeze' or percepts[k] == 'Stench' or percepts[k] == 'Safe'):
                        b = coordinates[k]
                        agent = ww[b[0]][b[1]]
                        if agent not in explored:
                            print(agent)
                            WumpusAlgo(b[0],b[1])
            for k in range(len(percepts)):
                b = []
                if(percepts[k] != 'PIT' and percepts[k] != 'Wumpus'):
                    b = coordinates[k]
                    agent = ww[b[0]][b[1]]
                    if agent not in explored:
                        print(agent)
                        WumpusAlgo(b[0],b[1])
            
        if agent is 'Breeze':
            explored.append(ww[i][j])
            percepts = []
            coordinates = []
            check[i][j] = 'OK'
            moves(i,j)
            for k in range(0,4):
                if actions[k][0]!='':
                    percepts.append(ww[actions[k][0]][actions[k][1]])
                    coordinates.append(actions[k])
            print(percepts)
            print(coordinates)
            for k in range(len(percepts)):
                a = []
                b = []
                if(percepts[k] == 'Unknown'):
                    percepts[k] = 'PIT'
                    b = coordinates[k]
                    print(b)
                    ww[b[0]][b[1]] = percepts[k]
            print(percepts)
            for k in range(len(percepts)):
                b = []
                if(percepts[k] == 'Gold'):
                    b = coordinates[k]
                    agent = ww[b[0]][b[1]]
                    if agent not in explored:
                        print(agent)
                        WumpusAlgo(b[0],b[1])
                if(percepts[k] != 'PIT' and percepts[k] != 'Wumpus'):
                    if(percepts[k] == 'Breeze' or percepts[k] == 'Stench' or percepts[k] == 'Safe'):
                        b = coordinates[k]
                        agent = ww[b[0]][b[1]]
                        if agent not in explored:
                            print(agent)
                            WumpusAlgo(b[0],b[1])
            for k in range(len(percepts)):
                b = []
                if(percepts[k] != 'PIT' and percepts[k] != 'Wumpus'):
                    b = coordinates[k]
                    agent = ww[b[0]][b[1]]
                    if agent not in explored:
                        print(agent)
                        WumpusAlgo(b[0],b[1])
            
        if agent is 'Stench':
            explored.append(ww[i][j])
            percepts = []
            coordinates = []
            check[i][j] = 'OK'
            moves(i,j)
            for k in range(0,4):
                if actions[k][0]!='':
                    percepts.append(ww[actions[k][0]][actions[k][1]])
                    coordinates.append(actions[k])
            print(percepts)
            print(coordinates)
            for k in range(len(percepts)):
                a = []
                b = []
                if(percepts[k] == 'Unknown'):
                    percepts[k] = 'Stench'
                    b = coordinates[k]
                    ww[b[0]][b[1]] = percepts[k]
                if(percepts[k] == 'PIT'):
                    percepts[k] = 'Safe'
                    b = coordinates[k]
                    ww[b[0]][b[1]] = percepts[k]
            print(percepts)
            for k in range(len(percepts)):
                b = []
                if(percepts[k] == 'Gold'):
                    b = coordinates[k]
                    agent = ww[b[0]][b[1]]
                    if agent not in explored:
                        print(agent)
                        WumpusAlgo(b[0],b[1])
                if(percepts[k] != 'PIT' and percepts[k] != 'Wumpus'):
                    if(percepts[k] == 'Breeze' or percepts[k] == 'Stench' or percepts[k] == 'Safe'):
                        b = coordinates[k]
                        agent = ww[b[0]][b[1]]
                        if agent not in explored:
                            print(agent)
                            WumpusAlgo(b[0],b[1])
            for k in range(len(percepts)):
                b = []
                if(percepts[k] != 'PIT' and percepts[k] != 'Wumpus'):
                    b = coordinates[k]
                    agent = ww[b[0]][b[1]]
                    if agent not in explored:
                        print(agent)
                        WumpusAlgo(b[0],b[1])

        if agent is 'Safe':
            explored.append(ww[i][j])
            percepts = []
            coordinates = []
            check[i][j] = 'OK'
            moves(i,j)
            for k in range(0,4):
                if actions[k][0]!='':
                    percepts.append(ww[actions[k][0]][actions[k][1]])
                    coordinates.append(actions[k])
            print(percepts)
            print(coordinates)
            for k in range(len(percepts)):
                b = []
                if(percepts[k] == 'Gold'):
                    b = coordinates[k]
                    agent = ww[b[0]][b[1]]
                    if agent not in explored:
                        print(agent)
                        WumpusAlgo(b[0],b[1])
                if(percepts[k] != 'PIT' and percepts[k] != 'Wumpus'):
                    if(percepts[k] == 'Breeze' or percepts[k] == 'Stench' or percepts[k] == 'Safe'):
                        b = coordinates[k]
                        agent = ww[b[0]][b[1]]
                        if agent not in explored:
                            print(agent)
                            WumpusAlgo(b[0],b[1])
            for k in range(len(percepts)):
                b = []
                if(percepts[k] != 'PIT' and percepts[k] != 'Wumpus'):
                    b = coordinates[k]
                    agent = ww[b[0]][b[1]]
                    if agent not in explored:
                        print(agent)
                        WumpusAlgo(b[0],b[1])
WumpusAlgo(0, 0)
