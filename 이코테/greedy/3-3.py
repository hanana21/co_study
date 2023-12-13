# 문제: 가장 큰 숫자 카드 뽑기 
#       행의 가장 작은 수 중에 가장 큰 수 선택하기 

# 풀이: 입력 받은 list에서 가장 최소값을 새로운 리스트에 저장한다. 저장된 값 중 최대값을 불러낸다.

n,m = map(int,input().split())
result = []
for i in range(n): # 한줄씩 입력 받기 
    data = list(map(int,input().split()))
    min_data = min(data)
    result.append(min_data)

print(max(result))
