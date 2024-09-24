from itertools import permutations


class Solution:
    nums = [1,2,3]
    def permute(self, nums: list[int]) -> list[list[int]]:
        list = []
        for i in permutations(nums, len(nums)):
            list.append(i)

        return list

solution = Solution()
nums = [1, 2, 3]
list = solution.permute(nums)  # 인스턴스를 통해 메서드 호출
print(list)