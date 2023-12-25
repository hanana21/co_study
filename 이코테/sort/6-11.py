# 성적이 낮은 순서로 학생 출력하기 
n = int(input())
array =[]
for i in range(n):
    input_data = input().split()
    array.append((input_data[0],int(input_data[1]))) #튜플형저장,숫자는 int형 저장
def setting(student):
    return student[1]
array = sorted(array,key=setting)
for student in array:
    print(student[0],end=' ')

#람다함수 사용 : 익명의 함수
array = sorted(array,key=lambda student:student[1]) #lamda 매개변수 : 결과
for student in array:
    print(student[0], end=' ')



