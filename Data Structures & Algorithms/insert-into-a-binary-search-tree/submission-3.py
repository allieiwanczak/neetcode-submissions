# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def insert(node, v):
            if node is None:
                return TreeNode(v)
            if v< node.val:
                node.left = insert(node.left, v)
            elif v> node.val:
                node.right = insert(node.right, v)
            return node
       
        return insert(root, val)