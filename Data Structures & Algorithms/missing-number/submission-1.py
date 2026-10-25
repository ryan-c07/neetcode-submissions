class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        expected = (max(nums)*(max(nums)+1))/2
        actual = 0
        for num in nums:
            actual += num
        if (int(expected - actual) == 0 and 0 in nums):
            return max(nums)+1
        return int(expected - actual)