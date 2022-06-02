"""
请实现一个函数按照之字形顺序打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右到左的顺序打印，第三行再按照从左到右的顺序打印，其他行以此类推。 

 

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
  [20,9],
  [15,7]
]
 

 

 提示： 

 
 节点总数 <= 1000 
 
 Related Topics 树 广度优先搜索 二叉树 👍 230 👎 0

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
                if cur_layer % 2 == 1:
                    res.append(tmp_layer[::-1])
                else:
                    res.append(tmp_layer)
                cur_layer = layer
                tmp_layer = [tmp.val]
            if tmp.left:
                stack.append((tmp.left, layer+1))
            if tmp.right:
                stack.append((tmp.right, layer+1))

        if tmp_layer:
            if cur_layer % 2 == 1:
                res.append(tmp_layer[::-1])
            else:
                res.append(tmp_layer)
        return res
# leetcode submit region end(Prohibit modification and deletion)
