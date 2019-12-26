class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            difference = target - nums[i]
            candidate_nums = nums[i+1:]
            if difference in candidate_nums:
                return [i, candidate_nums.index(difference) + i + 1]
