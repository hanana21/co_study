# 이진 탐색 : 반으로 쪼개면서 탐색 
#             내부 데이터가 정렬되어 있어야 사용 가능(이런경우 빠르게 찾을수 있다)
#             이진 탐색 코테 단골 문제니까 무조건 외우슈
#             범위가 2000만 넘어가면 접근해보슈
# 방법: 시작점과 끝점 중간점(시+끝/2의 버림)지정 후 target과 중간점 크기 비교 
#       만약 target < 중간점이면 끝점을 중간점 앞으로 옮김
#       다시 새로운 중간점과 target비교 만약 target>중간점이라면 시작점을 중간점 뒤로 옮긴다.
#       다시 반복하고 중간점이 target과 같아지면 종료 
# 시간 복잡도 : O(logN)
# 소스코드1(재귀함수)
def binary_search(array,target,start,end):
    if start>end:
        return None
    mid = (start+end)//2 # 중간점(//: 몫연산자)
    if target > array[mid]:
        return binary_search(start,target,mid+1,end)
    elif target < array[mid]:
        return binary_search(start,target,start,mid-1)
    elif target == array[mid]:
        return mid+1
# n,target입력받기 
input_data = input().split()
n = int(input_data[0])
target = int(input_data[1])
#전체원소 입력받기
array = list(map(int,input().split()))

#수행결과출력 
result = binary_search(array,target,0,n-1)
if result == None:
    print("없슈")
else:
    print(result)

# 소스코드2(반복문이용)
def binary_search2(array,target,start,end):
    while start<=end:
        mid = (start+end)//2
        if array[mid] == target:
            return mid+1
        elif array[mid] > target:
            end = mid-1
        elif array[mid] < target:
            start = mid+1
    return None

    