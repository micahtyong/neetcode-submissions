# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Just 1, Just 2, Just 3, 1 and 2, 1 and 3, 1 2 and 3
# Include left, exclude left
# Include right, exclude right

# [1,-2,-3,1,3,-2,null,-1]
#     1
#. -2. -3
# 1. 3 -2 null
#-1

class Solution:
    # Runtime: O(n) where n is amount of nodes in tree
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        # Returns max that can connect to parent, and max that cannot connect
        def dfs(root) -> tuple:
            if root.left == None and root.right == None:
                print("leaf", root.val, 0)
                return root.val, float('-inf') # maybe incorrect
            
            res, res_exc = root.val, float('-inf')
            if root.left:
                left_conn, left_exc = dfs(root.left)
                left_with_curr = root.val + left_conn
                res = max(res, left_with_curr)
                res_exc = max(res_exc, left_conn, left_exc)
            
            if root.right:
                right_conn, right_exc = dfs(root.right)
                right_with_curr = root.val + right_conn
                res = max(res, right_with_curr)
                res_exc = max(res_exc, right_conn, right_exc)
            
            if root.left and root.right:
                include_both = left_conn + right_conn + root.val
                res_exc = max(res_exc, include_both)
            
            print(res, res_exc, root.val)
            return (res, res_exc)

        res, res_exc = dfs(root)
        return max(res, res_exc)
        
        
