"""
给定一个二叉树的 根节点 root，请找出该二叉树的 最底层 最左边 节点的值。 

 假设二叉树中至少有一个节点。 

 

 示例 1: 

 

 
输入: root = [2,1,3]
输出: 1
 

 示例 2: 

 

 
输入: [1,2,3,4,null,5,6,null,null,7]
输出: 7
 

 

 提示: 

 
 二叉树的节点个数的范围是 [1,10⁴] 
 -2³¹ <= Node.val <= 2³¹ - 1 
 

 

 注意：本题与主站 513 题相同： https://leetcode-cn.com/problems/find-bottom-left-tree-value/
 
 Related Topics 树 深度优先搜索 广度优先搜索 二叉树 👍 25 👎 0

"""


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        res = []
        if not root:
            return None
        stack = [(root, 0)]
        count = 0
        while stack:
            cur_node, cur_layer = stack.pop(0)
            if cur_layer > count:
                res = [cur_node.val]
                count = cur_layer
            else:
                res.append(cur_node.val)
            if cur_node.left:
                stack.append((cur_node.left, cur_layer + 1))
            if cur_node.right:
                stack.append((cur_node.right, cur_layer + 1))

        return res[0]
# leetcode submit region end(Prohibit modification and deletion)
