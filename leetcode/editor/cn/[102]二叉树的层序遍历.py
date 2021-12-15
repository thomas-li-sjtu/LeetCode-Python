# 给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。 
# 
#  
# 
#  示例： 
# 二叉树：[3,9,20,null,null,15,7], 
# 
#  
#     3
#    / \
#   9  20
#     /  \
#    15   7
#  
# 
#  返回其层序遍历结果： 
# 
#  
# [
#   [3],
#   [9,20],
#   [15,7]
# ]
#  
#  Related Topics 树 广度优先搜索 二叉树 
#  👍 1075 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # 用嵌套的队列实现
        if not root:
            return []
        result = []
        queue = [[root]]
        while queue:
            tmp_layer = queue.pop(0)
            new_layer = []
            layer_val = []
            while tmp_layer:
                tmp_node = tmp_layer.pop(0)
                if tmp_node.left:
                    new_layer.append(tmp_node.left)
                if tmp_node.right:
                    new_layer.append(tmp_node.right)
                layer_val.append(tmp_node.val)
            if new_layer:
                queue.append(new_layer)
            result.append(layer_val)
        return result
# leetcode submit region end(Prohibit modification and deletion)
