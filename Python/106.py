class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not postorder:
            return None
        root = TreeNode(postorder[-1])
        n = inorder.index(root.val)
        root.left = self.buildTree(inorder[:n],postorder[:n])
        root.right = self.buildTree(inorder[n+1:],postorder[n:-1])
        return root
