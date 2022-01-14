class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        k=set(range(1, len(nums) + 1)) - set(nums)
        return k
