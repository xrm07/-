a,b,c,d,e,f=map(int,input().split())
g,h,i,j,k,l=map(int,input().split())


if abs(f-l)<abs(f-c):
    if abs(a-g)<abs(d-j):
        if abs(d-g)<abs(d-a):
            print("Yes")
        else:
            print("No")
    else:
        if abs(d-j)<abs(d-a):
            print("Yes")
        else:
            print("No")
else:
    print("No")
