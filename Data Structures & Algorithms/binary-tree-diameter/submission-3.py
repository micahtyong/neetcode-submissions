# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        # Compute diameter as we calculate tree heights.
        def heightOfTree(root) -> int:
            nonlocal res
            if root == None:
                return 0
            leftHeight = heightOfTree(root.left)
            rightHeight = heightOfTree(root.right)

            currDiameter = leftHeight + rightHeight
            res = max(res, currDiameter)

            return 1 + max(leftHeight, rightHeight)

        heightOfTree(root)
        return res