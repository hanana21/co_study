# 7-5 집합 자료형 이용 
# set(): 순서X, 중복X 
n = int(input())
parts = set(map(int,input().split()))

m = int(input())
requested_parts = list(map(int,input().split()))

for i in requested_parts:
    if i in parts:
        print('yes',end =' ')
    else: 
        print('no',end =' ')