N=int(input())
S=input()
T=input()
s=[]
cnt=0
while True:
    if S.count("W")!=T.count("W") or S.count("B")!=T.count("B") :
        break
    else:
        for i in range(N//2):
            s.append(S[i:i+2])
        for i in range(N//2):
            if T[i:i+2] in S:
                cnt+=1
            else:
                print(-1)
                exit()
        print(cnt)
        break