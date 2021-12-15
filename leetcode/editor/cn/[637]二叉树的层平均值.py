# 给定一个非空二叉树, 返回一个由每层节点平均值组成的数组。 
# 
#  
# 
#  示例 1： 
# 
#  输入：
#     3
#    / \
#   9  20
#     /  \
#    15   7
# 输出：[3, 14.5, 11]
# 解释：
# 第 0 层的平均值是 3 ,  第1层是 14.5 , 第2层是 11 。因此返回 [3, 14.5, 11] 。
#  
# 
#  
# 
#  提示： 
# 
#  
#  节点值的范围在32位有符号整数范围内。 
#  
#  Related Topics 树 深度优先搜索 广度优先搜索 二叉树 
#  👍 302 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        if not root:
            return None
        queue = [[root]]
        node_val = []
        while queue:
            layer = queue.pop(0)
            new_layer = []
            layer_node = []
            while layer:
                tmp_node = layer.pop(0)
                if tmp_node.left:
                    new_layer.append(tmp_node.left)
                if tmp_node.right:
                    new_layer.append(tmp_node.right)
                layer_node.append(tmp_node.val)
            if layer_node:
                node_val.append(sum(layer_node)/float(len(layer_node)))
            if new_layer:
                queue.append(new_layer)
        return node_val

# leetcode submit region end(Prohibit modification and deletion)
