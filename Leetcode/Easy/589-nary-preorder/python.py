"""
# Return preorder of nary tree
Input: root = [1,null,3,2,4,null,5,6]
Output: [1,3,5,6,2,4]
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

Recursive is trivial, try iterative

TC:- O(N)
SC:- O(N)
"""
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        """def recursive_preorder(node):
            if not node:
                return
            output.append(node.val)
            for child in node.children:
                recursive_preorder(child)
        
        output = []
        recursive_preorder(root)
        return output"""
        stack = []
        output = []
        if root:
            stack.append(root.val)
        while stack:
            node = stack.pop()
            output.append(node.val)
            for child in reversed(node.children): 
                # to mimic order which is suitable for system stack
                stack.append(child)
        return output