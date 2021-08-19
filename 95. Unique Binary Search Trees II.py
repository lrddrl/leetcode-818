class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def help(self,start, end):
        if start > end:
            return[None]

        result = []
        for current_root in range(start, end +1):
            left = self.help(start, current_root - 1)
            right = self.help(current_root+1, end)

            for l in left:
                for r in right:
                    root = TreeNode(current_root)
                    root.left = l
                    root.right = r
                    result.append(root)
        return result 
           
    def generateTrees(self, n):
        if n == 0 :
            return[]
        return self.help(1,n)


c = Solution(3)

print(c.help(3))
