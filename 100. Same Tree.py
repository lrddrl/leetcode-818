class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

    def isSameTree(self, p : TreeNode, q: TreeNode) -> bool:
        if p is None and q is None:
            return True
        
        if p is not None and q is not None:
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

        return False




a1 = TreeNode()
print(a1.isSameTree([1,2,1], [1,1,2]))