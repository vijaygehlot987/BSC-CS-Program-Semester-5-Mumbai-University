import copy
sol = []
def nQueenProblem(queens, n, occupied):
    global sol
    if n == 0:
        if not beingAttacked(occupied):

            sol.append(copy.deepcopy(occupied))
        return
    else:
        for i in range(queens):
            if i not in occupied:
                if not beingAttacked(occupied):
                    occupied.append(i)
                    nQueenProblem(queens, n - 1, occupied)
                    occupied.pop()

def beingAttacked(positions):
    attack = False
    for i in range(len(positions)):
        
        flag = False
        for j in range(1 , len(positions) - i):
            var1 = var2 = None
            if positions[i] - j >= 0:
                var1 = positions[i] - j
            if positions[i] + j <= len(positions):
                var2 = positions[i] + j
            
            if var1 is not None and var2 is not None:
                if positions[i+j] == var1 or positions[i+j] == var2:
                    flag = True
                    break
            elif var1 is not None:
                if positions[i+j] == var1:
                    flag = True
                    break
            else:
                if positions[i+j] == var2:
                    flag = True
                    break
        if flag:    
            attack = True
            break     
    return attack

board = queens = 5

nQueenProblem(queens, board, [])
print("No. of solutions : ", len(sol))

for i in range(len(sol)):
    matrix = [["-" for i in range(board)] for j in range(board)]
    for pos in range(len(sol[i])):
        matrix[pos][sol[i][pos]] = 1
    print("Board:")
    for row in matrix:
        for val in row:
            print(val, end="  ")
        print()
    print()
        
