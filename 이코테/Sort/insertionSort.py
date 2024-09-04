#삽입 정렬 : 데이터가 거의 정렬돼있을 때 효과적
#두번째 데이터부터 시작함. 첫번째는 정렬돼있다고 판단해서.

array=[7,5,9,0,3,1,6,2,4,8]

for i in range(1, len(array)):
    for j in range(i, 0, -1):
        if array[j]<array[j-1] : array[j], array[j-1] = array[j-1], array[j]
        else : break

print(array)