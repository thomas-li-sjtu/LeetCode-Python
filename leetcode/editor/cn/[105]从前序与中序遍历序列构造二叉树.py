"""
给定两个整数数组 preorder 和 inorder ，其中 preorder 是二叉树的先序遍历， inorder 是同一棵树的中序遍历，请构造二叉树并返回
其根节点。 

 

 示例 1:

 
输入: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
输出: [3,9,20,null,null,15,7]
 

 示例 2: 

 
输入: preorder = [-1], inorder = [-1]
输出: [-1]
 

 

 提示: 

 
 1 <= preorder.length <= 3000 
 inorder.length == preorder.length 
 -3000 <= preorder[i], inorder[i] <= 3000 
 preorder 和 inorder 均 无重复 元素 
 inorder 均出现在 preorder 
 preorder 保证 为二叉树的前序遍历序列 
 inorder 保证 为二叉树的中序遍历序列 
 
 Related Topics 树 数组 哈希表 分治 二叉树 👍 1551 👎 0

"""

# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
from typing import List


# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        # 先序遍历先根节点，再左节点，再右节点，因此输出时根在起始，左边先是左孩子，再是右孩子
        # 中序遍历先左节点，再根节点，再右节点，因此输出时根在中间某位置，其左边是左孩子，右边是右孩子
        # preorder第一个元素是根节点，在inoder中找到根节点位置，记为index，index左边都是左子树，右边都是右子树，从而知道preorder中左右子树起始位置
        if not preorder and not inorder:
            return None
        root_val = preorder[0]
        root_index_in = 0
        for i, val in enumerate(inorder):
            if val == root_val:
                root_index_in = i
                break
        left_inorder = inorder[0:root_index_in]
        right_inorder = inorder[root_index_in+1:]
        left_preorder = preorder[1:1+root_index_in]
        right_preorder = preorder[1+root_index_in:]

        root = TreeNode(val=root_val)
        root.left = self.buildTree(left_preorder, left_inorder)
        root.right = self.buildTree(right_preorder, right_inorder)

        return root
# leetcode submit region end(Prohibit modification and deletion)
