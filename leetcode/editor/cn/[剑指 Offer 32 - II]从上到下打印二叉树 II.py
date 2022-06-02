"""
从上到下按层打印二叉树，同一层的节点按从左到右的顺序打印，每一层打印到一行。 

 

 例如: 
给定二叉树: [3,9,20,null,null,15,7], 

     3
   / \
  9  20
    /  \
   15   7
 

 返回其层次遍历结果： 

 [
  [3],
  [9,20],
  [15,7]
]
 

 

 提示： 

 
 节点总数 <= 1000 
 

 注意：本题与主站 102 题相同：https://leetcode-cn.com/problems/binary-tree-level-order-
traversal/ 
 Related Topics 树 广度优先搜索 二叉树 👍 229 👎 0

"""

# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        if not root:
            return res
        stack = [(root, 0)]
        cur_layer = 0
        tmp_layer = []
        while stack:
            tmp, layer = stack.pop(0)
            if layer == cur_layer:
                tmp_layer.append(tmp.val)
            else:
                cur_layer = layer
                res.append(tmp_layer)
                tmp_layer = [tmp.val]
            if tmp.left:
                stack.append((tmp.left, layer+1))
            if tmp.right:
                stack.append((tmp.right, layer+1))
        if tmp_layer:
            res.append(tmp_layer)
        return res
# leetcode submit region end(Prohibit modification and deletion)
