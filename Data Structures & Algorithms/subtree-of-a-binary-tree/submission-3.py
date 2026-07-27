# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def same(self,s,r):
        if not s and not r:
            return True
        if r and s and r.val == s.val:
            return self.same(s.left,r.left) and self.same(s.right,r.right)
        return False

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if not subRoot:
            return True
        
        if self.same(subRoot,root):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)