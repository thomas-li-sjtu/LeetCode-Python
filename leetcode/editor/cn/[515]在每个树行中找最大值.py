"""
给定一棵二叉树的根节点 root ，请找出该二叉树中每一层的最大值。 

 

 示例1： 

 

 
输入: root = [1,3,2,5,3,null,9]
输出: [1,3,9]
 

 示例2： 

 
输入: root = [1,2,3]
输出: [1,3]
 

 

 提示： 

 
 二叉树的节点个数的范围是 [0,10⁴] 
 -2³¹ <= Node.val <= 2³¹ - 1 
 

 
 Related Topics 树 深度优先搜索 广度优先搜索 二叉树 👍 234 👎 0

"""

# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
from typing import Optional, List
import math


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        res = [-math.inf]
        if not root:
            return []
        stack = [(root, 0)]

        while stack:
            cur_node, cur_layer = stack.pop(0)
            if cur_node.left:
                stack.append((cur_node.left, cur_layer+1))
            if cur_node.right:
                stack.append((cur_node.right, cur_layer+1))
            if len(res)-1 >= cur_layer:
                res[cur_layer] = max(res[cur_layer], cur_node.val)
            else:
                res.append(cur_node.val)
        return res

# leetcode submit region end(Prohibit modification and deletion)
