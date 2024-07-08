countA=0
counta=0
S=str(input())

for i  in range(len(S)):
    if S[i].isupper():
        countA+=1
    elif S[i].islower():
        counta+=1


if countA>counta:
    print(S.upper())
else:
    print(S.lower())