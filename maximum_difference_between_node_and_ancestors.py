# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def find_maximum(node, maximum, minimum):
            if not node:
                return 0
            diff = max(abs(node.val-maximum), abs(node.val-minimum))
            maximum = max(maximum, node.val)
            minimum = min(minimum, node.val)
            return max(diff, find_maximum(node.left, maximum, minimum), find_maximum(node.right, maximum, minimum))
        return find_maximum(root, root.val, root.val)
    
