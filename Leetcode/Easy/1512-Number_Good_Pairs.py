# num[i] == num[j] and i < j

class Solution:
    def numIdenticalPairs(self, nums):
        seen = {}
        ans = 0
        for i in range(len(nums)):
            seen[i] = 1
            for j in range(i, len(nums)):
                if j in seen.keys():
                    ans += 1
        return ans