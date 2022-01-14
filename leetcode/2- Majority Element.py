class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=len(nums)
        new_dict = defaultdict(int)
        for i in nums: 
            new_dict[i] += 1
        
        for j in new_dict: 
            if new_dict[j] >n//2:
                return j
        
