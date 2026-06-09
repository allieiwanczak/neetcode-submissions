# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def delete(node,num):
            if node is None:
                return None
            if num < node.val:
                node.left = delete(node.left, num)
            elif num > node.val:
                node.right= delete(node.right, num)
            else:
                # no child - left
                if node.left is None:
                    return node.right
                
                #no child - right
                if node.right is None:
                    return node.left
                
                # 2 children
                succ = node.right
                while succ.left:
                    succ = succ.left
                node.val = succ.val
                node.right = delete(node.right, succ.val)
            return node

        return delete(root,key)
