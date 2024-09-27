#해시테이블
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        max_len = 0
        subst={} #해시테이블 지정

        if not s:
            return 0
        for index in range(len(s)):
            if s[index] in subst:
                start = max(start,subst[s[index]]+1)
            subst[s[index]] = index
            max_len = max(max_len, index-start+1)

        return max_len

s = "abcabcbb"
solution = Solution()
result = solution.lengthOfLongestSubstring(s)
print(result)