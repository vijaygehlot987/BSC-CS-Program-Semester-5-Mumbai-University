visited=[]
f_limit=1000
f_limit_city=None
l1=[]
l2=[]
l3=[]
l4=[]

h={
   'arad':366,
   'zerind':374,
   'oradea':380,
   'sibiu':253,
   'fagaras':176,
   'bucharest':0,
   'rimnicu':193,
   'pitesti':100,
   'timisora':329
   }
graph={
       'arad':['zerind','sibiu','timisora'],
       'zerind':['arad','oradea'],
       'oradea':['zerind','sibiu'],
       'sibiu':['arad','oradea','fagaras','rimnicu'],
       'fagaras':['sibiu','bucharest'],
       'bucharest':['fagaras','pitesti'],
       'rimnicu':['sibiu','pitesti'],
       'pitesti':['bucharest','rimnicu'],
        'timisora':['arad']
}
g={
       'arad':[75,140,118],
       'zerind':[75,71],
       'oradea':[71,151],
       'sibiu':[140,151,99,80],
       'fagaras':[99,211],
       'bucharest':[211,101],
       'rimnicu':[80,97],
       'pitesti':[101,97],
       'timisora':[118]
   }
def rbfs(src,dest,x,l1,l2,l3,f_limit,f_limit_city):
    
        l4=[]
        
    
        if src==dest:
            print("destination reached")
            return True
        else:
            print("expanding",src)
            print("generating",graph[src])
            for i in range (0,len(g[src])):
                
                l2.append(graph[src][i])
                l1.append(x+g[src][i]+h[graph[src][i]])
                #l4.append(x+g[src][i]+h[graph[src][i]])
                l3.append(g[src][i]+x)
                
                
            print("f_limit city is ",f_limit_city,"and f_limit is "+str(f_limit))
            print()
            for i in range(len(l1)):
                print(l1[i],"-",l2[i])
                print()
            if(f_limit<=min(l1)):
                
                temp=f_limit_city
            else:
                temp=l2[l1.index(min(l1))] 
            x=l3[l1.index(min(l1))]
            print("Selected ",temp,"-",min(l1))

            l2.remove(temp)
            l1.pop(l1.index(min(l1)))
            l3.remove(x)
            
            
            f_limit=min(l1)
            f_limit_city=l2[l1.index(min(l1))]
            
            return rbfs(temp,dest,x,l1,l2,l3,f_limit,f_limit_city)

rbfs('fagaras','pitesti',0,l1,l2,l3,f_limit,f_limit_city)
