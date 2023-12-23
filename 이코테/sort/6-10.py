# 내림차 순으로 정렬하는 프로그램 
m = int(input())
array = []
for i in range(m):
    array.append(int(input()))
#정렬라이브러리
array = sorted(array,reverse=True)
for i in array:
    print(i, end=' ')
#계수정렬
count = [0] * (max(array)+1)
for i in array:
    count[i] += 1
for j in range(max(array),0,-1) :
    for k in range(count[j]):
        print(j,end= ' ')
   