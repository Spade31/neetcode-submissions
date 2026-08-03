class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        krish = {}

        for i , j in enumerate(nums):
            diff = target - j
            if diff in krish:
                return [krish[diff], i]
            krish[j] = i
        return
