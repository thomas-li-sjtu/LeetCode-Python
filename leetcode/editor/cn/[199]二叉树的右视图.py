"""
给定一个二叉树的 根节点 root，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。 

 

 示例 1: 

 

 
输入: [1,2,3,null,5,null,4]
输出: [1,3,4]
 

 示例 2: 

 
输入: [1,null,3]
输出: [1,3]
 

 示例 3: 

 
输入: []
输出: []
 

 

 提示: 

 
 二叉树的节点个数的范围是 [0,100] 
 -100 <= Node.val <= 100 
 
 Related Topics 树 深度优先搜索 广度优先搜索 二叉树 👍 667 👎 0

"""


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        if not root:
            return []
        stack = [(root, 0)]
        val_save = []
        while stack:
            tmp_node, tmp_layer = stack.pop(0)
            val_save.append((tmp_node.val, tmp_layer))
            if tmp_node.left:
                stack.append((tmp_node.left, tmp_layer + 1))
            if tmp_node.right:
                stack.append((tmp_node.right, tmp_layer + 1))
        flag = 0
        print(val_save)
        for i in range(len(val_save)):
            tmp_layer = val_save[i][1]
            if tmp_layer != flag:
                res.append(val_save[i - 1][0])
                flag = tmp_layer
        res.append(val_save[-1][0])

        return res

# leetcode submit region end(Prohibit modification and deletion)
