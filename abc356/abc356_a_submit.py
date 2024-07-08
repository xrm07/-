N,L,R = map(int,input().split())
l=list(range(1,N+1))
leftlist=l[0:L-1]
#print(leftlist)
rightlist=l[R:N]
#print(rightlist)
sublist=l[L-1:R]
#l = [1, 2, 3, 4, 5]
count = len(sublist)
print(sublist)
# 外側のループで回数を減らしながら繰り返す
for j in range(count - 1):
    # 内側のループで要素を入れ替える
    for i in range(count - 1 - j):
        # 要素を入れ替え
        a = sublist[i]
        b = sublist[i + 1]
        sublist[i] = b
        sublist[i + 1] = a

# 結果を出力
resultlist=leftlist+sublist+rightlist
print(*resultlist)