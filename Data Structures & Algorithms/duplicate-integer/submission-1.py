class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dupes = {}
        for num in nums:
            dupes[num] = dupes.get(num, 0) + 1
        return any(value > 1 for value in dupes.values())
