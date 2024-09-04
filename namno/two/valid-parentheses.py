class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i == '(' or i== '{' or i=='[':
                stack.append(i)
            else :
                if not stack:
                    return False
                else :
                    x = stack.pop()
                    if x == '(' and i ==')':
                        continue
                    elif x == '{' and i =='}':
                        continue
                    elif x == '[' and i ==']':
                        continue
                    else : return False
        if stack : return False
        else: return True
       