"""
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历结果。如果是则返回 true，否则返回 false。假设输入的数组的任意两个数字都互不相同。 

 

 参考以下这颗二叉搜索树： 

      5
    / \
   2   6
  / \
 1   3 

 示例 1： 

 输入: [1,6,3,2,5]
输出: false 

 示例 2： 

 输入: [1,3,2,6,5]
输出: true 

 

 提示： 

 
 数组长度 <= 1000 
 
 Related Topics 栈 树 二叉搜索树 递归 二叉树 单调栈 👍 527 👎 0

"""
from typing import List


class TreeNode:

    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:
        if not postorder:
            return True
        inorder = sorted(postorder)
        try:
            root = self.build_tree(postorder=postorder, inorder=inorder)
        except:
            return False

        tmp_stack = [root]
        while tmp_stack:
            tmp_node = tmp_stack.pop(0)
            if tmp_node.left:
                if tmp_node.left.val > tmp_node.val:
                    return False
                else:
                    tmp_stack.append(tmp_node.left)
            if tmp_node.right:
                if tmp_node.right.val < tmp_node.val:
                    return False
                else:
                    tmp_stack.append(tmp_node.right)
        return True

    def build_tree(self, postorder: List[int], inorder: List[int]) -> TreeNode:
        if not len(postorder):
            return None
        if len(postorder) == 2:
            tmp_node = TreeNode(postorder[-1])
            if tmp_node.val == inorder[0]:
                tmp_node.left = None
                tmp_node.right = TreeNode(inorder[1])
            else:
                tmp_node.left = TreeNode(inorder[0])
                tmp_node.right = None
            return tmp_node
        if len(postorder) == 1:
            return TreeNode(postorder[0])

        root = TreeNode(postorder[-1])
        index = inorder.index(root.val)
        left_inorder = inorder[:index]
        right_inordr = inorder[index+1:]
        left_postorder = postorder[:index]
        right_postorder = postorder[index:-1]
        root.left = self.build_tree(postorder=left_postorder, inorder=left_inorder)
        root.right = self.build_tree(postorder=right_postorder, inorder=right_inordr)

        return root

# leetcode submit region end(Prohibit modification and deletion)
