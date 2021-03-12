# Input: nums = [-10,-3,0,5,9]
# Output: [0,-3,9,-10,null,5]
# Runtime :- 100th percentile
# memory usage :- 100th percentile
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if nums == None or len(nums) == 0:
            return 
        return self.recursiveBST(nums, 0, len(nums) - 1)
        
    def recursiveBST(self, nums, left, right):
        if left > right:
            return
        else:
            mid = left + (right - left) // 2
            current = TreeNode(val = nums[mid])
            current.left = self.recursiveBST(nums, left, mid-1)
            current.right = self.recursiveBST(nums, mid+1, right)
            return current
 
