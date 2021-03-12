# TC:- O(N)
# SC:- O(H)
# Runtime :- 87.62%
# Memory :- 47.06%

class Solution:
    current_node = TreeNode()
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            root.left = None
            self.current_node.right = root
            self.current_node = root
            self.inorder(root.right)
            
    def increasingBST(self, root: TreeNode) -> TreeNode:
        ansNode = TreeNode()
        self.current_node = ansNode
        self.inorder(root)
        return ansNode.right
