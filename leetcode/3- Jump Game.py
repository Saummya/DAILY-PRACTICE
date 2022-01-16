class Solution:
    def canJump(self, nums: List[int]) -> bool:
            '''
            goal=len(nums)-1
            for i in range(len(nums)-1,-1,-1):
                if i+nums[i]>i:
                    goal=i

            return True if goal==0 else False
            '''
            goal = 0
            for i in range(len(nums)):
                if i > goal:
                    return False
                goal = max(goal, nums[i] + i)
            return True
