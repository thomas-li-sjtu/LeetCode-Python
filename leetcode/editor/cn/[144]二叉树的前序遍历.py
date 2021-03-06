# 给你二叉树的根节点 root ，返回它节点值的 前序 遍历。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：root = [1,null,2,3]
# 输出：[1,2,3]
#  
# 
#  示例 2： 
# 
#  
# 输入：root = []
# 输出：[]
#  
# 
#  示例 3： 
# 
#  
# 输入：root = [1]
# 输出：[1]
#  
# 
#  示例 4： 
# 
#  
# 输入：root = [1,2]
# 输出：[1,2]
#  
# 
#  示例 5： 
# 
#  
# 输入：root = [1,null,2]
# 输出：[1,2]
#  
# 
#  
# 
#  提示： 
# 
#  
#  树中节点数目在范围 [0, 100] 内 
#  -100 <= Node.val <= 100 
#  
# 
#  
# 
#  进阶：递归算法很简单，你可以通过迭代算法完成吗？ 
#  Related Topics 栈 树 深度优先搜索 二叉树 
#  👍 674 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.node_list = []
        self.traversal(root)
        self.node_list = [i for i in self.node_list if i]
        return self.node_list

    def traversal(self, root):
        if root:
            self.node_list.append(root.val)
            self.node_list.append(self.traversal(root.left))
            self.node_list.append(self.traversal(root.right))
# leetcode submit region end(Prohibit modification and deletion)
