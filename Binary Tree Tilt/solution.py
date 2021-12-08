# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        total = 0
        def helper(root):
            nonlocal total
            
            if not root:
                return 0
            left = helper(root.left)
            right = helper(root.right)
            tilt = abs(left - right)
            
            total += tilt
            
            return left+right+root.val
        helper(root)
        return total
