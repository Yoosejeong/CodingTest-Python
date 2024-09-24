from itertools import combinations
class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        list = []
        for i in range(1, n+1):
            list.append(i)
        
        result = []
        for i in combinations(list, k):
            result.append(i)

        return result
    
solution = Solution()
result = solution.combine(4,2)
print(result)