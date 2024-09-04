def solution(s):
    stack = []
    answer = 0

    for i in s:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if not stack:
                return -1  
            t = stack.pop()
            if t == '(':  
                answer += 1


    if stack:
        return -1  

    return answer