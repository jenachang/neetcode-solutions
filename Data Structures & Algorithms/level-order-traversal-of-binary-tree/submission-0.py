# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


#1 DO I HAVE TO MAKE AN IMPORT STATEMENT?
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
        else:
         queue = deque([root])
         result = []
         
         while (len(queue) > 0):
            n = len(queue)
            new_level = []
            for _ in range(n):
                node = queue.popleft()
                new_level.append(node.val)
                for child in [node.left, node.right]:
                    if child == None:        
                        continue
                    else:
                        queue.append(child)
            result.append(new_level)
         return result  
                
