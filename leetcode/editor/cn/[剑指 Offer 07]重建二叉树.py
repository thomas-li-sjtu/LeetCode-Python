"""
输入某二叉树的前序遍历和中序遍历的结果，请构建该二叉树并返回其根节点。 

 假设输入的前序遍历和中序遍历的结果中都不含重复的数字。 

 

 示例 1: 

 
Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]
 

 示例 2: 

 
Input: preorder = [-1], inorder = [-1]
Output: [-1]
 

 

 限制： 

 0 <= 节点个数 <= 5000 

 

 注意：本题与主站 105 题重复：https://leetcode-cn.com/problems/construct-binary-tree-from-
preorder-and-inorder-traversal/ 
 Related Topics 树 数组 哈希表 分治 二叉树 👍 811 👎 0

"""

# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
from typing import List


# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder and not inorder:
            return None
        if len(preorder) == 2:
            tmp_node = TreeNode(preorder[0])
            if preorder[0] == inorder[0]:
                tmp_node.left = None
                tmp_node.right = TreeNode(inorder[1])
            else:
                tmp_node.left = TreeNode(inorder[0])
                tmp_node.right = None
            return tmp_node
        if len(preorder) == 1:
            tmp_node = TreeNode(preorder[0])
            tmp_node.left = None
            tmp_node.right = None
            return tmp_node

        root = TreeNode(preorder[0])
        index = inorder.index(root.val)
        left_inorder = inorder[:index]
        right_inorder = inorder[index+1:]
        left_preorder = preorder[1:1+len(left_inorder)]
        right_preorder = preorder[1+len(left_inorder):]
        root.left = self.buildTree(preorder=left_preorder, inorder=left_inorder)
        root.right = self.buildTree(preorder=right_preorder, inorder=right_inorder)

        return root
# leetcode submit region end(Prohibit modification and deletion)
