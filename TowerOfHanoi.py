def ToH(n,fromm,to,aux): #from,to,aux rod name
    if n==1:
        print("move disk 1 form  "+fromm+ " to rod "+to)
        return
    ToH(n-1,fromm,aux,to)
    print("move disk "+str(n)+" from rod "+fromm+" to ROD "+to)
    ToH(n-1,aux,to,fromm)
n=8
ToH(n,'A','C','B')
    
