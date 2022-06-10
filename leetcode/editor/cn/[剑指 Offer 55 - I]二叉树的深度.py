"""
输入一棵二叉树的根节点，求该树的深度。从根节点到叶节点依次经过的节点（含根、叶节点）形成树的一条路径，最长路径的长度为树的深度。 

 例如： 

 给定二叉树 [3,9,20,null,null,15,7]， 

     3
   / \
  9  20
    /  \
   15   7 

 返回它的最大深度 3 。 

 

 提示： 

 
 节点总数 <= 10000 
 

 注意：本题与主站 104 题相同：https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/
 
 Related Topics 树 深度优先搜索 广度优先搜索 二叉树 👍 191 👎 0

"""

# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        res = []
        stack = [(root, 1)]
        while stack:
            tmp_node, tmp_depth = stack.pop()
            if not tmp_node.left and not tmp_node.right:
                res.append(tmp_depth)
            if tmp_node.left:
                stack.append((tmp_node.left, tmp_depth+1))
            if tmp_node.right:
                stack.append((tmp_node.right, tmp_depth+1))
        return max(res)

# leetcode submit region end(Prohibit modification and deletion)
