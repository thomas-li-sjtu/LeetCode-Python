"""
给定一个二叉树的 根节点 root，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。 

 

 示例 1: 

 

 
输入: [1,2,3,null,5,null,4]
输出: [1,3,4]
 

 示例 2: 

 
输入: [1,null,3]
输出: [1,3]
 

 示例 3: 

 
输入: []
输出: []
 

 

 提示: 

 
 二叉树的节点个数的范围是 [0,100] 
 -100 <= Node.val <= 100 
 

 

 注意：本题与主站 199 题相同：https://leetcode-cn.com/problems/binary-tree-right-side-view/ 

 Related Topics 树 深度优先搜索 广度优先搜索 二叉树 👍 30 👎 0

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
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        stack = [(root, 0)]
        layer_dict = {}
        res = []
        while stack:
            cur_node, cur_layer = stack.pop(0)
            if cur_node.left:
                stack.append((cur_node.left, cur_layer + 1))
            if cur_node.right:
                stack.append((cur_node.right, cur_layer + 1))
            if layer_dict.get(cur_layer):
                layer_dict[cur_layer].append(cur_node.val)
            else:
                layer_dict[cur_layer] = [cur_node.val]

        for i in range(1000):
            if not layer_dict.get(i):
                break
            res.append(layer_dict[i][-1])
        return res
# leetcode submit region end(Prohibit modification and deletion)
