# 给定一个二叉树，返回其节点值的锯齿形层序遍历。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。 
# 
#  例如： 
# 给定二叉树 [3,9,20,null,null,15,7], 
# 
#  
#     3
#    / \
#   9  20
#     /  \
#    15   7
#  
# 
#  返回锯齿形层序遍历如下： 
# 
#  
# [
#   [3],
#   [20,9],
#   [15,7]
# ]
#  
#  Related Topics 树 广度优先搜索 二叉树 
#  👍 541 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
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
            if len(result) % 2 == 0:
                result.append(layer_val)
            else:
                result.append(layer_val[::-1])

        return result
# leetcode submit region end(Prohibit modification and deletion)
