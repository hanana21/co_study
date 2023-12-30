# 7-5 계수정렬 통해 풀기
# 방법: 부품종류가 모두 담길수 있는 크기의 리스트를 만들어서 입력받은 가게 부품에 해당하는 인덱스 값을 1로 바꾼다.
#       손님이 요구하는 부품들중에 리스트에 1로 담겨있다면 yes 아니면 no 출력  

n = int(input())
array = [0] * 1000001 # 범위가 1 <= n <= 1000000

for i in input().split():
    array[int(i)] = 1

m = int(input())
requested_parts = list(map(int,input().split()))
for i in requested_parts:
    if array[i] == 1:
        print('yes', end =' ')
    else:
        print('no', end =' ')


