#정수 N이 입력되면 00시00분00초부터 N시 59분 59초까지 3 포함되는 경우의수

N = int(input())

count = 0
for i in range(N+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j)+ str(k):
                count +=1

print(count)