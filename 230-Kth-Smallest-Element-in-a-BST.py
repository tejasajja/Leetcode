# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        def inorder(root):
            if root is None:
                return []
            else:
                return inorder(root.left) + [root.val] + inorder(root.right)
        v = inorder(root)
        return v[k-1]

        