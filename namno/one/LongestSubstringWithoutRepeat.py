
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        list = []
        #list에 문자열s를 담는다. 
        for i in s:
            list.append(i)
        
        #투포인터로 해결하기위해 one, two 정의
        #max는 최댓값을 지정해두기 위해서
        one = 0
        two = 1
        max = 0
        answer=  0
        #문자열이 0인 경우("") 0을 리턴
        if len(s) == 0:
            return 0

        #one이 two보다 작고, two가 list의 길이보다 작을때까지 반복
        while one<two and two <= len(list)-1:
            #만약에 list[one]이 list[two]와 다르고, list[two]가 list[one]부터 list[two]사이에 없는 값이라면 substring개수를 증가시킬 수 있다.
            if list[one]!=list[two] and list[two] not in list[one:two]:
                #answer은 two-one으로 두 간격의 길이
                answer = two-one
                #만약 max가 answer보다 작으면 max값이 answer값이 된다. (최댓값 저장하기위해)
                if max <= answer : max= answer
                #two를 증가시켜 substring개수를 증가
                two+=1
            #만약 list[one]과 list[two]의 값이 같다면 one과 two모두 증가시켜준다. one에서부터 연산 불가능. 
            elif list[one] == list[two]:
                one +=1
                two +=1
            #만약 list[one]과 list[two]의 값이 다르지만 list[one]에서 list[two]사이에 값이 나온적이 있다면 one을 증가시켜준다.
            else :
                one +=1
        return max+1

s =  "pwwkew"
solution = Solution()
result = solution.lengthOfLongestSubstring(s)
print(result)