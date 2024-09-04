#투포인터
def solution(nums, target):
	answer = 0
	start = 0
	end = len(nums)-1
	nums.sort()
	while start<end:
		if nums[start] + nums[end] == target:
			answer = answer + 1
			start = start + 1
			end = end - 1
		elif nums[start] + nums[end] > target:
			end = end - 1
		else : 
			start = start + 1
	return answer