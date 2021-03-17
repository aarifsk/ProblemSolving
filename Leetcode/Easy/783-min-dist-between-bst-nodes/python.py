# Runtime 87.36 %
# Memory usage 99.84%
class Solution:
    previous = -float('inf')
    result = float('inf')

    def minDiffInBST(self, root):
        if root.left:
            self.minDiffInBST(root.left)
        self.result = min(self.result, root.val - self.previous)
        self.previous = root.val
        if root.right:
            self.minDiffInBST(root.right)
        return self.result