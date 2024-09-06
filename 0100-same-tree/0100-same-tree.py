class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Check if both trees are empty (both p and q are None)
        if not p and not q:
            return True
        
        # Check if both trees are non-empty and have the same root value
        if p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        
        # Return False if none of the above conditions are met
        return False