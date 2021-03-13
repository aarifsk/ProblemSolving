"""
given a BST and target val,
find the value and return the subtree
Input: root = [4,2,7,1,3], val = 2
Output: [2,1,3]

TC:- O(N)
SC:-O(1)
"""
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        current_node = root
        while current_node:
            if val == current_node.val:
                return current_node
            elif val < current_node.val:
                current_node = current_node.left
            else:
                current_node = current_node.right