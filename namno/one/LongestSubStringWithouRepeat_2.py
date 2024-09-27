#해시테이블
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        max_len = 0
        subst={} #해시테이블 지정

        if not s:
            return 0
        for end in range(len(s)):
            if s[end] in subst:
                start = max(start,subst[s[end]]+1)
            subst[s[end]] = end 
            max_len = max(max_len, end-start+1)

        return max_len

s = "abcabcbb"
solution = Solution()
result = solution.lengthOfLongestSubstring(s)
print(result)