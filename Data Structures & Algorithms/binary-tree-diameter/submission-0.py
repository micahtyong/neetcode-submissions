# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root == None or (root.left == None and root.right == None):
            print("Return early, leaf node or none")
            return 0

        # Brute force: Max of height between left and right trees.
        def heightOfTree(root) -> int:
            if root == None or (root.left == None and root.right == None):
                return 0
            leftHeight = heightOfTree(root.left)
            rightHeight = heightOfTree(root.right)
            return 1 + max(leftHeight, rightHeight)

        leftHeight, rightHeight = 0, 0
        if root.left:
            leftHeight = 1 + heightOfTree(root.left)
        if root.right:
            rightHeight = 1 + heightOfTree(root.right)
        diameter = leftHeight + rightHeight

        leftDiameter = self.diameterOfBinaryTree(root.left)
        rightDiameter = self.diameterOfBinaryTree(root.right)

        return max(diameter, leftDiameter, rightDiameter)