x = int(input())

#첫번째 라인부터 시작
line = 1 
#첫번째 라인의 끝 번호는 1번
end_line = 1

#line의 끝자리 보다 크면 반복하기
while x > end_line:
    line += 1
    end_line += line

#line에서 몇 번째인지 계산하기
position = x-(end_line-line)

#라인이 홀수면
if line%2==1:
    down = position
    up = line-position+1
#라인이 짝수면
else :
    up = position
    down = line-position+1
print(f'{up}/{down}')

    