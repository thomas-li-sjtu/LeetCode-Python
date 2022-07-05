"""
给定一棵二叉树的根节点 root ，请找出该二叉树中每一层的最大值。 

 

 示例1： 

 
输入: root = [1,3,2,5,3,null,9]
输出: [1,3,9]
解释:
          1
         / \
        3   2
       / \   \  
      5   3   9 
 

 示例2： 

 
输入: root = [1,2,3]
输出: [1,3]
解释:
          1
         / \
        2   3
 

 示例3： 

 
输入: root = [1]
输出: [1]
 

 示例4： 

 
输入: root = [1,null,2]
输出: [1,2]
解释:      
           1 
            \
             2     
 

 示例5： 

 
输入: root = []
输出: []
 

 

 提示： 

 
 二叉树的节点个数的范围是 [0,10⁴] 
 -2³¹ <= Node.val <= 2³¹ - 1 
 

 

 注意：本题与主站 515 题相同： https://leetcode-cn.com/problems/find-largest-value-in-each-
tree-row/ 
 Related Topics 树 深度优先搜索 广度优先搜索 二叉树 👍 26 👎 0

"""

# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        stack = [(root, 0)]
        res = {}

        while stack:
            cur_node, cur_layer = stack.pop(0)
            if cur_node.left:
                stack.append((cur_node.left, cur_layer + 1))
            if cur_node.right:
                stack.append((cur_node.right, cur_layer + 1))
            if res.get(cur_layer):
                res[cur_layer].append(cur_node.val)
            else:
                res[cur_layer] = [cur_node.val]

        max_num = [0] * len(res)
        for key, value in res.items():
            max_num[key] = max(value)
        return max_num

# leetcode submit region end(Prohibit modification and deletion)
