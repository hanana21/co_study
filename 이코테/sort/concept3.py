# 퀵 정렬 파이선 장점 살리기 
array = [5,7,9,0,3,1,6,2,4,8]
def quick_sort(array):
    # 리스트가 하나 이하의 원소만 담고 있다면 종료 
    if len(array) <= 1:
        return array
    pivot = array[0]
    tail = array[1:] # 피벗을 제외한 나머지 요소
    left_side=[x for x in tail if x<=pivot]# 피벗보다 작은 요소들모임=> 피벗의 왼쪽으로 둘것
    right_side=[x for x in tail if x > pivot]# 피벗보다 큰 요소들모임=> 피벗의 오른쪽으로 둘것
    #분할 완료
    return quick_sort(left_side)+[pivot]+quick_sort(right_side)
print(quick_sort(array))

