
# 3. 퀵 정렬
#   : 기준 데이터(피벗)를 선택하고 그 기준보다 큰데이터와 작은 데이터의 위치를 바꾼다. 
#     => 피벗(첫데이터)를 기준으로 왼쪽부터 피벗보다 큰데이터와 오른쪽부터 피벗보다 작은 데이터 선택해 바꿔준다.
#        엇갈린 경우 피벗과 작은데이터를 바꿔준다.(분할 완료)
#        왼쪽 오른쪽도 피벗을 기준으로 정렬해준다.
#   - 가장 많이 사용되는 
#   - 피벗을 설정하는 방식에 따라 여러 종류로 나누어지지만 호어분할을 이용할것(첫데이터를 피벗으로)
#   - 평균적으로 O(NlogN)의 시간 복잡도 가짐, 최악의 경우O(N2)=>이미 정렬되어있을때,하지만 기본정렬 라이브러리 이용하면 O(NlogN)보장해줌 

# 퀵정렬 소스 코드 (직관적)
array = [5,7,9,0,3,1,6,2,4,8]
def quick_sort(array,start,end):
    if start >= end:
        return
    # 각 부분 시작점, 피벗 정의해주기 
    pivot = start
    left = start+1 # 왼쪽 부분  
    right = end #오른쪽 부분 
    while left <= right:
        # 피벗보다 큰 데이터 인덱스 찾을 때까지 left+1
        while left <= end and array[left] <= array[pivot]:  
            left += 1
        # 피벗보다 작은 데이터 인덱스 찾을 때까지 right-1
        while right > start and array[right] >= array[pivot]: 
            right -= 1
        if left > right: # 찾은 인덱스가 서로 엇갈린 경우 피벗이랑 작은수(오른) 바꾸기 
            array[right],array[pivot] = array[pivot],array[right] 
        else: # 아닌경우 작은쪽(오른) 큰쪽(왼) 바꾸기
            array[right],array[left] = array[left],array[right] 
    # 분활된 부분 다시 퀵정렬 
    quick_sort(array,start,right-1)
    quick_sort(array,right+1,end)
quick_sort(array,0,len(array)-1)
print(array)
    
        

