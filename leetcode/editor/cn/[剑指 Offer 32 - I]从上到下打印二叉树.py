"""
从上到下打印出二叉树的每个节点，同一层的节点按照从左到右的顺序打印。 

 

 例如: 
给定二叉树: [3,9,20,null,null,15,7], 

     3
   / \
  9  20
    /  \
   15   7
 

 返回： 

 [3,9,20,15,7]
 

 

 提示： 

 
 节点总数 <= 1000 
 
 Related Topics 树 广度优先搜索 二叉树 👍 202 👎 0

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
    def levelOrder(self, root: TreeNode) -> List[int]:
        res = []
        if not root:
            return res
        stack = [root]
        while stack:
            tmp = stack.pop(0)
            res.append(tmp.val)
            if tmp.left:
                stack.append(tmp.left)
            if tmp.right:
                stack.append(tmp.right)
        return res

# leetcode submit region end(Prohibit modification and deletion)
