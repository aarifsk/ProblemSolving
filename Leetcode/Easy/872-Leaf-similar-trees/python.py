# Runtime :- 92nd percentile
# Space complexity :- 9th percentile

# input :- 2 trees
# [3,5,1,6,2,9,8,null,null,7,4]
# [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]

# output :- boolean

# Definition for a binary tree node
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        def dfs(node):
            if node:
                if not node.right and not node.left:
                    yield node.val
                yield from dfs(node.left)
                yield from dfs(node.right)
                    
        return list(dfs(root1)) == list(dfs(root2)) 