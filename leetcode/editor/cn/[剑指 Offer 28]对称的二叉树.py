"""
请实现一个函数，用来判断一棵二叉树是不是对称的。如果一棵二叉树和它的镜像一样，那么它是对称的。 

 例如，二叉树 [1,2,2,3,4,4,3] 是对称的。 

 1 
 / \ 
 2 2 
 / \ / \ 
3 4 4 3 
但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的: 

 1 
 / \ 
 2 2 
 \ \ 
 3 3 

 

 示例 1： 

 输入：root = [1,2,2,3,4,4,3]
输出：true
 

 示例 2： 

 输入：root = [1,2,2,null,3,null,3]
输出：false 

 

 限制： 

 0 <= 节点个数 <= 1000 

 注意：本题与主站 101 题相同：https://leetcode-cn.com/problems/symmetric-tree/ 
 Related Topics 树 深度优先搜索 广度优先搜索 二叉树 👍 347 👎 0

"""

# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True

        def create_dup_tree(node: TreeNode):
            if not node:
                return None
            new_node = TreeNode(x=node.val)
            new_node.left = create_dup_tree(node.left)
            new_node.right = create_dup_tree(node.right)
            return new_node

        new_root = create_dup_tree(root)

        def mirror(node: TreeNode):
            if node.left:
                mirror(node.left)
            if node.right:
                mirror(node.right)
            node.left, node.right = node.right, node.left

        mirror(root)

        stack = [root]
        new_stack = [new_root]
        while stack and new_stack:
            tmp = stack.pop(0)
            new_tmp = new_stack.pop(0)

            if tmp.val != new_tmp.val:
                return False
            if (
                    (tmp.left and not new_tmp.left) or
                    (tmp.right and not new_tmp.right) or
                    (not tmp.left and new_tmp.left) or
                    (not tmp.right and new_tmp.right)
            ):
                return False

            if tmp.right:
                stack.append(tmp.right)
                new_stack.append(new_tmp.right)
            if tmp.left:
                stack.append(tmp.left)
                new_stack.append(new_tmp.left)
        return True

# leetcode submit region end(Prohibit modification and deletion)
