def solution(prices):
    answer = [0] * len(prices)
    stack = []
    for i in range(len(prices)):
        while stack and prices[i]<stack[-1][1] : #스택이 차있고, 스택 top(이전 주식)이 현재 주식 가격보다 크다면? -> 가격이 떨어졌다. 가격이 떨어지면 answer를 확정할 수 있다. 더 볼필요없다. 이미 떨어진순간 끝났기때문
            answer[stack[-1][0]] = i-stack[-1][0]
            stack.pop()
        stack.append([i, prices[i]]) #스택에 인덱스인 i, 값인 prices[i] 넣기
        
    while stack:
        answer[stack[-1][0]] = (len(prices)-1)-(stack[-1][0])
        stack.pop()
    return answer

prices = [1,2,3,2,3]

answer = solution(prices)
print(answer)