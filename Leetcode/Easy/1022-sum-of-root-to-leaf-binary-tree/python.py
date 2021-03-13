"""
Input: root = [1,0,1,0,1,0,1]
Output: 22
Explanation: (100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22
SC:- O(N)
TC:- O(N)
"""
class Solution:
    def sumRootToLeaf(self, root: TreeNode, running_sum=0) -> int:
        if not root:
            return running_sum
        running_sum = running_sum * 2 + root.val
        if root.left or root.right:
            x = self.sumRootToLeaf(root.left, running_sum)
            y = self.sumRootToLeaf(root.right, running_sum)
            return x + y
        else:
            return running_sum