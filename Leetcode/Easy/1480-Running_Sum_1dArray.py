class Solution:
    def runningSum(self, nums):
        running_sum = 0
        ans = []
        for i in nums:
            running_sum += i
            ans.append(running_sum)
        return ans
