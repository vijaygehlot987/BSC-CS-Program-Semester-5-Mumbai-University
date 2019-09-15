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
l=1
p=[]
def idfs(s,d,l):
    if(l>0):
        p.append(s)
        if s==d:
            return l
        x=0
        for i in graph[s]:
            if i not in p:
                x=idfs(i,d,l-1)
            if x>0:
                return x
        del p[-1]
        return 0
    else:
        return 0
a="A"
b="J"

x=idfs(a,b,l)
while True:
    if x==1:
        print("destination found at level",l)
        print(p)
        break
    l=l+1
    x=idfs(a,b,l)
