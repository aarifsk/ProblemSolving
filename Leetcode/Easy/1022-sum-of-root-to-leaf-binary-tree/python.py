"""
Input: root = [1,0,1,0,1,0,1]
Output: 22
Explanation: (100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22
SC:- O(N)
TC:- O(N)
"""
class Solution:
    def sumRootToLeaf(self, root: TreeNode, running_sum=0) -> int:
        def getSum(root,running_sum=0):
            if(root == None):
                return running_sum
            else:
                running_sum=running_sum*2+root.val
                node=0
                if(root.left):
                    node+=getSum(root.left,running_sum)
                if(root.right):
                    node+=getSum(root.right,running_sum)
                return running_sum if node==0 else node
        return getSum(root)
