def solution(prices):
    n = len(prices)
    answer = [0] * n
    for i in range(n):
        count = 0
        for j in range(i+1, n):
            count += 1
            if prices[i]>prices[j]:
                break
        answer[i] = count
    return answer