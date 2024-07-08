N,X,Y,Z=map(int,input().split())

if Y>X:
     L=list(range(X,Y+1))
else:
     L=list(range(Y,X+1))
    
if Z in L:
     print("Yes")
else:
     print("No")

    
