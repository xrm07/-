A,B=map(int,input().split())
list=[A,B]

#print(list)
if A==B:
    print("-1")
elif "1" not in list :
    print("1")
elif "2" not in list :
    print("2")
elif "3" not in list :
    print("3")
# 1,2,3の中からA,Bではない数字を出力する 