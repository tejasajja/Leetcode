# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = 0
        def dep(root):
            if root ==None:
                return 0
            left = dep(root.left)
            right = dep(root.right)


            self.ans = max(left + right, self.ans)

            
            return max(left,right) +1

        dep(root)
        return self.ans
        