#list=[1,2,3,4,5]
#for i in range(len(list)-1):
 #   for i in range(len(list)-1):
 #       list[i]=list[len(list)-1]
 #       list[i]=list[i+1]
    
#print(list)

#result=list[:]
#print(result)
#N,L,R = map(int,input().split())
#l=list(range(1,N+1))
l = [1, 2, 3, 4, 5]
count = len(l)

# 外側のループで回数を減らしながら繰り返す
for j in range(count - 1):
    # 内側のループで要素を入れ替える
    for i in range(count - 1 - j):
        # 要素を入れ替え
        a = l[i]
        b = l[i + 1]
        l[i] = b
        l[i + 1] = a

# 結果を出力
print(*l)
