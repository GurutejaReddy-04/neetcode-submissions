# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root):

        self.diameter = 0

        def depth(node):
            if not node:
                return 0

            left = depth(node.left)
            right = depth(node.right)

            # update longest path
            self.diameter = max(self.diameter, left + right)

            # return height of subtree
            return 1 + max(left, right)

        depth(root)
        return self.diameter
        