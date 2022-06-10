"""
输入一棵二叉树的根节点，判断该树是不是平衡二叉树。如果某二叉树中任意节点的左右子树的深度相差不超过1，那么它就是一棵平衡二叉树。 

 

 示例 1: 

 给定二叉树 [3,9,20,null,null,15,7] 

 
    3
   / \
  9  20
    /  \
   15   7 

 返回 true 。 
 
示例 2: 

 给定二叉树 [1,2,2,3,3,null,null,4,4] 

 
       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
 

 返回 false 。 

 

 限制： 

 
 0 <= 树的结点个数 <= 10000 
 

 注意：本题与主站 110 题相同：https://leetcode-cn.com/problems/balanced-binary-tree/ 

 
 Related Topics 树 深度优先搜索 二叉树 👍 281 👎 0

"""


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        # # 自上而下
        # def search_depth(node: TreeNode):
        #     if not node:
        #         return 0
        #     res = []
        #     stack = [(node, 1)]
        #     while stack:
        #         tmp_node, tmp_depth = stack.pop()
        #         if not tmp_node.left and not tmp_node.right:
        #             res.append(tmp_depth)
        #         if tmp_node.left:
        #             stack.append((tmp_node.left, tmp_depth + 1))
        #         if tmp_node.right:
        #             stack.append((tmp_node.right, tmp_depth + 1))
        #     return max(res)
        #
        # if not root:
        #     return True
        # stack = [root]
        # while stack:
        #     tmp_node = stack.pop()
        #     tmp_node_left_depth = search_depth(tmp_node.left)
        #     tmp_node_right_depth = search_depth(tmp_node.right)
        #     if abs(tmp_node_right_depth - tmp_node_left_depth) > 1:
        #         return False
        #     if tmp_node.left:
        #         stack.append(tmp_node.left)
        #     if tmp_node.right:
        #         stack.append(tmp_node.right)
        # return True

        # 自底向上，类似后序遍历
        def height(root: TreeNode) -> int:
            if not root:
                return 0
            leftHeight = height(root.left)
            rightHeight = height(root.right)
            if leftHeight == -1 or rightHeight == -1 or abs(leftHeight - rightHeight) > 1:
                return -1
            else:
                return max(leftHeight, rightHeight) + 1

        return height(root) >= 0

# leetcode submit region end(Prohibit modification and deletion)
