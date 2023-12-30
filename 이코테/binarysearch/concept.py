# 순차 탐색: 리스트 안에 있는 특정 데이터를 찾기 위해 처음부터 차례대로 데이터를 확인하는 방법 
#            시간만 많다면 무조건 찾을 수 있다는 장점 
#            보통 정렬되지 않은 리스트에서 데이터를 찾아야할때 사용
#            순서대로 탐색 진행 최악의 경우 시간 복잡도 O(N)
# 순차 탐색 소스코드 
def sequential_search(n,target,array): # 순차 탐색을 통해 target과 동일한 인덱스 반환 
    for i in range(n):
        if array[i] == target:
            return i+1
print("생성할 원소갯수를 입력한 다음 한칸 띄우고 찾을 문자열을 입력하세요")
input_data = input().split()
n = int(input_data[0])
target = input_data[1] #이미 str로 들어와서 바꿔줄 필요 없음

print("앞서적은 원소갯수 만큼 문자열을 입력하세요. 구분은 띄어쓰기 한 칸으로 합니다")
array = input().split()#공백을 기준으로 분할하여 list로 반환

# 순차탐색 수행
print(sequential_search(n,target,array))
    