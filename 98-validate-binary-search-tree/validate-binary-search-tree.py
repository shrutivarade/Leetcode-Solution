# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        

        def dfs(root, currmax, currmin):
            if root == None :
                return True
            

            # if(
            #     (root.left != None and (root.left.val <= currmin or root.left.val >= currmax or root.left.val == root.val)) 
            #     or
            #     (root.right != None and (root.right.val >= currmax or root.right.val <= currmin or root.right.val == root.val ))
            # ):

            if not (currmin < root.val < currmax):
                return False
            

            return dfs(root.left, root.val, currmin) and dfs(root.right, currmax, root.val)



        return dfs(root, float('inf'), float('-inf'))

        
