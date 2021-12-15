# 计算给定二叉树的所有左叶子之和。 
# 
#  示例： 
# 
#  
#     3
#    / \
#   9  20
#     /  \
#    15   7
# 
# 在这个二叉树中，有两个左叶子，分别是 9 和 15，所以返回 24 
# 
#  
#  Related Topics 树 深度优先搜索 广度优先搜索 二叉树 
#  👍 370 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        leaf_val = []
        stack = [root]
        while stack:
            tmp = stack.pop()
            if tmp.left:
                if not tmp.left.left and not tmp.left.right:
                    leaf_val.append(tmp.left.val)
                stack.append(tmp.left)
            if tmp.right:
                stack.append(tmp.right)
        return sum(leaf_val)

# leetcode submit region end(Prohibit modification and deletion)
