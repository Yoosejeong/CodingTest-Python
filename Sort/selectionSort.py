#선택정렬 : 가장 작은 데이터를 앞으로 보내기를 N-1번 반복하기
array = [7,5,9,0,3,1,6,2,4,8]

for i in range(len(array)): #array끝까지 반복하기
    min_index = i #가장 작은 원소의 인덱스로 지정
    for j in range(i+1, len(array)):#i+1번째부터 끝까지 반복하기
        if array[min_index]>array[j] : #만약 min_index의 값이 j보다 크면
            min_index = j #j가 최솟값의 인덱스가 된다.
        #반복해서 최솟값을 찾아준다.
    array[i], array[min_index] = array[min_index], array[i] #스와프

print(array)