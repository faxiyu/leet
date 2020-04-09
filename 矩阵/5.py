class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index, num in enumerate(nums):
            res = target - num
            if res in nums:
                if res == num and nums.count(res) > 1:
                    return [index, nums.index(res, index+1)]
                if res != num:
                    return [index, nums.index(res)]