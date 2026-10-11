# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> list[list[int]]:
        result = []

        def dfs(node, path, total):
            if not node:
                return
            
            total += node.val
            path.append(node.val)

            if not node.left and not node.right:
                if total == targetSum:
                    result.append(path[:])
            else:
                dfs(node.left, path, total)
                dfs(node.right, path, total)
            path.pop()
        
        dfs(root, [], 0)
        return result