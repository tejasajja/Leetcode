# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.prev = None
        
        def inorder(root):
            if root is None:
                return True
            # Check the left subtree
            if not inorder(root.left):
                return False
            # Current node value must be greater than the previous node value (strictly increasing)
            if self.prev is not None and root.val <= self.prev:
                return False
            # Update prev to the current node value
            self.prev = root.val
            # Check the right subtree
            return inorder(root.right)
        
        return inorder(root)