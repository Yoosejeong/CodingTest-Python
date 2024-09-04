#N명으 ㅣ학생 정보가 있다. 학생 정보는 학생의 이름, 성적으로 구분됨.
#각 학생의 이름, 성적정보 주어졌을때 성적 낮은 순서대로 학생의 이름을 출력
N = int(input())
arr=[]

for i in range(N):
    input_data = input().split()
    arr.append((input_data[0], input_data[1]))

arr = sorted(arr, key = lambda student : student[1])

for student in arr:
    print(student[0], end=' ')